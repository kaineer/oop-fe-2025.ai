#!/usr/bin/env python3

"""
step-refs - проверка соответствия REF меток между кодом и метаданными
Использование:
  step-refs.py           - проверка текущего шага
  step-refs.py 02        - проверка шага 02
  step-refs.py 02 04     - проверка шагов с 02 по 04 включительно
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml


class StepRefsValidator:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.lesson = "07-update-list"  # Пока фиксируем урок 07, можно расширить

    def extract_refs_from_code(self, step_path: Path) -> Dict[str, Set[str]]:
        """Извлекает все REF метки из файлов шага"""
        code_refs = {}

        # Ищем все JS и HTML файлы
        for pattern in ["*.js", "*.html"]:
            for file_path in step_path.rglob(pattern):
                if file_path.is_file():
                    relative_path = str(file_path.relative_to(step_path))
                    try:
                        content = file_path.read_text(encoding="utf-8")
                        # Ищем REF метки в JS файлах
                        if file_path.suffix == ".js":
                            matches = re.findall(
                                r"//\s*REF:\s*([a-zA-Z0-9_-]+)", content
                            )
                            for match in matches:
                                if relative_path not in code_refs:
                                    code_refs[relative_path] = set()
                                code_refs[relative_path].add(match)
                        # Ищем REF метки в HTML файлах
                        elif file_path.suffix == ".html":
                            matches = re.findall(
                                r"<!--\s*REF:\s*([a-zA-Z0-9_-]+)\s*-->", content
                            )
                            for match in matches:
                                if relative_path not in code_refs:
                                    code_refs[relative_path] = set()
                                code_refs[relative_path].add(match)
                    except Exception as e:
                        print(f"⚠️  Ошибка чтения файла {file_path}: {e}")

        return code_refs

    def extract_refs_from_meta(self, step_number: str) -> Set[str]:
        """Извлекает REF ссылки из meta.yaml для конкретного шага"""
        meta_refs = set()
        meta_file = self.project_root / "lessons" / self.lesson / "meta.yaml"

        if not meta_file.exists():
            print(f"❌ Файл meta.yaml не найден: {meta_file}")
            return meta_refs

        try:
            with open(meta_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Парсим YAML
            data = yaml.safe_load(content)
            if not data or "project" not in data or "steps" not in data["project"]:
                print("⚠️  В meta.yaml не найдены шаги проекта")
                return meta_refs

            # Ищем нужный шаг
            target_step_path = f"src/step{step_number}"
            for step in data["project"]["steps"]:
                if step.get("path") == target_step_path and "actions" in step:
                    for action in step["actions"]:
                        refs = action.get("ref", [])
                        if isinstance(refs, str):
                            refs = [refs]
                        elif isinstance(refs, list):
                            # Обрабатываем вложенные структуры
                            processed_refs = []
                            for item in refs:
                                if isinstance(item, str):
                                    processed_refs.append(item)
                                elif isinstance(item, dict) and "ref" in item:
                                    nested_ref = item["ref"]
                                    if isinstance(nested_ref, str):
                                        processed_refs.append(nested_ref)
                                    elif isinstance(nested_ref, list):
                                        processed_refs.extend(nested_ref)
                            refs = processed_refs

                        for ref in refs:
                            if ref:  # Игнорируем пустые строки
                                meta_refs.add(ref)

        except yaml.YAMLError as e:
            print(f"❌ Ошибка парсинга YAML: {e}")
        except Exception as e:
            print(f"❌ Ошибка чтения meta.yaml: {e}")

        return meta_refs

    def check_step(
        self, step_number: str
    ) -> Tuple[Dict[str, Set[str]], Set[str], Set[str]]:
        """Проверяет один шаг и возвращает результаты"""
        step_path = (
            self.project_root / "lessons" / self.lesson / "src" / f"step{step_number}"
        )

        if not step_path.exists():
            print(f"❌ Шаг {step_number} не существует: {step_path}")
            return {}, set(), set()

        print(f"🔍 Проверка REF меток для шага {step_number}...")

        # Извлекаем метки из кода и meta.yaml
        code_refs_dict = self.extract_refs_from_code(step_path)
        meta_refs = self.extract_refs_from_meta(step_number)

        # Находим несоответствия
        unregistered_in_code = set()
        missing_in_code = set()

        # Проверяем каждую ссылку из meta.yaml
        for meta_ref in meta_refs:
            found = False
            # Разбираем ссылку на файл и метку
            if "@" in meta_ref:
                meta_file, meta_label = meta_ref.split("@", 1)
            else:
                meta_file = meta_ref
                meta_label = None

            # Ищем соответствующий файл в коде
            for code_file, code_labels in code_refs_dict.items():
                # Сравниваем файлы: полный путь или только имя файла
                if code_file == meta_file or code_file.endswith(f"/{meta_file}"):
                    if meta_label is None or meta_label in code_labels:
                        found = True
                        break

            if not found:
                missing_in_code.add(meta_ref)

        # Проверяем незарегистрированные метки в коде
        for code_file, code_labels in code_refs_dict.items():
            for code_label in code_labels:
                code_ref = f"{code_file}@{code_label}"
                # Проверяем, зарегистрирована ли метка в meta.yaml
                registered = False
                for meta_ref in meta_refs:
                    if "@" in meta_ref:
                        meta_file, meta_label = meta_ref.split("@", 1)
                        # Сравниваем файлы и метки
                        if (
                            code_file == meta_file
                            or code_file.endswith(f"/{meta_file}")
                        ) and code_label == meta_label:
                            registered = True
                            break

                if not registered:
                    unregistered_in_code.add(code_ref)

        return code_refs_dict, unregistered_in_code, missing_in_code

    def print_results(
        self,
        step_number: str,
        code_refs_dict: Dict[str, Set[str]],
        unregistered: Set[str],
        missing: Set[str],
    ):
        """Выводит результаты проверки"""
        print(f"\n📊 Результаты проверки для шага {step_number}:")

        # Подсчитываем общее количество меток
        total_code_refs = sum(len(labels) for labels in code_refs_dict.values())
        if total_code_refs:
            print(f"✅ Найдено меток в коде: {total_code_refs}")
        else:
            print("⚠️  В коде не найдено REF меток")

        if unregistered:
            print("⚠️  Незарегистрированные метки в коде:")
            for ref in sorted(unregistered):
                print(f"   - {ref}")

        if missing:
            print("❌ Отсутствующие метки в коде:")
            for ref in sorted(missing):
                print(f"   - {ref}")

        if not unregistered and not missing:
            print("🎉 Все REF метки соответствуют!")

    def get_last_step(self) -> str:
        """Находит последний шаг в уроке"""
        lesson_path = self.project_root / "lessons" / self.lesson / "src"
        steps = []

        if lesson_path.exists():
            for item in lesson_path.iterdir():
                if item.is_dir() and item.name.startswith("step"):
                    step_num = item.name[4:]  # Убираем 'step'
                    if step_num.isdigit():
                        steps.append(int(step_num))

        if not steps:
            raise ValueError(f"Не найдены шаги в уроке {self.lesson}")

        return f"{max(steps):02d}"

    def run(self, args: List[str]):
        """Основная логика выполнения"""
        print(f"🔍 Проверка REF меток для урока: {self.lesson}")

        if len(args) == 0:
            # Без параметров - проверяем последний шаг
            try:
                last_step = self.get_last_step()
                code_refs_dict, unregistered, missing = self.check_step(last_step)
                self.print_results(last_step, code_refs_dict, unregistered, missing)
            except ValueError as e:
                print(f"❌ {e}")
                sys.exit(1)

        elif len(args) == 1:
            # Один параметр - проверяем конкретный шаг
            step_number = args[0].zfill(2)  # Добавляем ведущий ноль если нужно
            code_refs_dict, unregistered, missing = self.check_step(step_number)
            self.print_results(step_number, code_refs_dict, unregistered, missing)

        elif len(args) == 2:
            # Два параметра - проверяем диапазон шагов
            start_step = int(args[0])
            end_step = int(args[1])

            for step in range(start_step, end_step + 1):
                step_number = f"{step:02d}"
                code_refs_dict, unregistered, missing = self.check_step(step_number)
                self.print_results(step_number, code_refs_dict, unregistered, missing)
                print()  # Пустая строка между шагами

        else:
            print("❌ Неверное количество параметров")
            print("Использование:")
            print("  step-refs.py           - проверка текущего шага")
            print("  step-refs.py 02        - проверка шага 02")
            print("  step-refs.py 02 04     - проверка шагов с 02 по 04 включительно")
            sys.exit(1)


def main():
    """Точка входа в программу"""
    try:
        validator = StepRefsValidator()
        validator.run(sys.argv[1:])
    except KeyboardInterrupt:
        print("\n⏹️  Проверка прервана пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
