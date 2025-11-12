# Краткий конспект занятия - Объектная модель браузера

## Ключевые концепции

### Основные объекты DOM
- **window** - глобальный объект браузера
- **document** - объект документа (DOM)
- **navigator** - информация о браузере

### Поиск элементов
- **querySelector** - поиск первого элемента по CSS-селектору
- **querySelectorAll** - поиск всех элементов по CSS-селектору
- **children** - дочерние элементы
- **parentElement** - родительский элемент
- **closest** - ближайший родитель по селектору

### Работа с классами и атрибутами
- **className** - строка с классами элемента
- **classList** - объект для работы с классами (add, remove, toggle, contains)
- **dataset** - доступ к data-атрибутам

### Модификация DOM
- **append** - добавление элементов
- **remove** - удаление элемента

## Примеры для демонстрации

### Получение доступа к элементам
```javascript
// По id
const elementById = document.getElementById('myId');

// По классу
const elementByClass = document.querySelector('.myClass');

// По тегу
const elementsByTag = document.querySelectorAll('div');
```

### Работа с querySelector
```javascript
// Все элементы с классом 'item'
const items = document.querySelectorAll('.item');

// Первый элемент списка
const firstItem = document.querySelector('ul li:first-child');

// Элемент с data-атрибутом
const dataElement = document.querySelector('[data-user-id="123"]');
```

### Изменение класса элемента
```javascript
const element = document.querySelector('.my-element');

// Через className
element.className = 'new-class';

// Через classList
element.classList.add('active');
element.classList.remove('inactive');
element.classList.toggle('hidden');
```

### Изменение стиля элемента
```javascript
const element = document.querySelector('.my-element');

element.style.color = 'red';
element.style.backgroundColor = '#f0f0f0';
element.style.fontSize = '16px';
```

### Удаление элемента
```javascript
const element = document.querySelector('.to-remove');

// Современный способ
element.remove();

// Старый способ
element.parentNode.removeChild(element);
```

## Интересные факты

- **jQuery** собирается выпустить 4ю версию, хотя современный JavaScript уже предоставляет аналогичные возможности

## Вопросы для обсуждения

1. В чем разница между querySelector и getElementById?
2. Когда использовать classList вместо className?
3. Почему querySelectorAll возвращает NodeList, а не массив?
4. В чем преимущества data-атрибутов?
5. Когда использовать append вместо innerHTML?
6. Почему важно использовать современные методы (remove, append)?

## Типичные ошибки

- Забывание проверки на null при поиске элементов
- Использование innerHTML для простого добавления текста
- Неправильное использование classList (например, add вместо toggle)
- Забывание event.preventDefault() в обработчиках событий
- Использование устаревших методов (getElementsByClassName вместо querySelector)

## Практические упражнения

### Задача 1: Получаем ссылку на элемент в списке
```javascript
const listItem = document.querySelector('ul li:first-child');
```

### Задача 2: Получаем ссылку на все элементы списка
```javascript
const allListItems = document.querySelectorAll('ul li');
```

### Задача 3: Получаем ссылку на tr если есть ссылка на td
```javascript
const td = document.querySelector('td');
const tr = td.closest('tr'); // или td.parentElement
```

### Задача 4: Считаем количество дочерних элементов
```javascript
const container = document.querySelector('.container');
const childCount = container.children.length;
```

## Дополнительные вопросы для проверки

- Найти все элементы с определенным data-атрибутом
- Добавить новый элемент в конец списка
- Удалить все элементы с классом 'to-remove'
- Переключить класс 'active' у кнопки при клике
- Получить значение data-атрибута и использовать его