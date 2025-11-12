# Полный конспект занятия - Функции в JavaScript

## Теория с примерами

### Введение в функции

Функции в JavaScript - это блоки кода, которые можно многократно вызывать для выполнения определенных задач. Они помогают организовать код, избежать повторений и сделать программу более читаемой.

### Способы создания функций

#### Function Declaration (Объявление функции)
```javascript
function sum(a, b) {
    return a + b;
}
```
- Поднимается (hoisted) - можно вызывать до объявления
- Имеет имя функции

#### Function Expression (Функциональное выражение)
```javascript
const multiply = function(a, b) {
    return a * b;
};
```
- Не поднимается - нельзя вызывать до объявления
- Может быть анонимной или именованной

#### Стрелочные функции (Arrow Functions)
```javascript
const divide = (a, b) => a / b;
```
- Более короткий синтаксис
- Не имеют своего `this`
- Не могут быть конструкторами
- Не имеют объекта `arguments`

#### Другие способы создания функций
```javascript
// Конструктор Function (не рекомендуется)
const greet = new Function('name', 'return "Hello, " + name');

// Методы объектов
const calculator = {
    add: function(a, b) { return a + b; },
    subtract(a, b) { return a - b; } // сокращенный синтаксис
};
```

### Вызов функций

#### Прямой вызов
```javascript
const result = sum(5, 3); // результат: 8
```

#### Вызов через call и apply
```javascript
function introduce(greeting) {
    return `${greeting}, меня зовут ${this.name}`;
}

const person = { name: 'Анна' };

// call - аргументы передаются по отдельности
introduce.call(person, 'Привет'); // "Привет, меня зовут Анна"

// apply - аргументы передаются массивом
introduce.apply(person, ['Здравствуйте']); // "Здравствуйте, меня зовут Анна"
```

#### Сохранение контекста с помощью bind
```javascript
const boundIntroduce = introduce.bind(person);
boundIntroduce('Привет'); // "Привет, меня зовут Анна"
```

### Контекст выполнения (this)

#### this в обычных функциях
```javascript
const obj = {
    name: 'Объект',
    getName: function() {
        return this.name; // this ссылается на obj
    }
};

obj.getName(); // "Объект"
```

#### this в стрелочных функциях
```javascript
const obj = {
    name: 'Объект',
    getName: () => {
        return this.name; // this берется из внешней области
    }
};

obj.getName(); // undefined (если вызвано в глобальной области)
```

### Детальный разбор синтаксиса функций

#### Параметры и возвращаемые значения
```javascript
function processData(input, options = {}) {
    // Параметры по умолчанию
    const { verbose = false } = options;
    
    if (verbose) {
        console.log('Обрабатываем:', input);
    }
    
    return input * 2; // Возвращаемое значение
}
```

#### Деструктуризация объектов в параметрах
```javascript
function createUser({ name, age, email = 'не указан' }) {
    return {
        username: name.toLowerCase(),
        age,
        email,
        createdAt: new Date()
    };
}

createUser({ name: 'Мария', age: 25 }); // {username: 'мария', age: 25, email: 'не указан', ...}
```

#### Деструктуризация массивов в параметрах
```javascript
function getFirstAndLast([first, , last]) {
    return { first, last };
}

getFirstAndLast(['яблоко', 'банан', 'апельсин']); // {first: 'яблоко', last: 'апельсин'}
```

#### Неопределенное количество аргументов (rest параметры)
```javascript
function sumAll(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

sumAll(1, 2, 3, 4, 5); // 15
```

## Пошаговые объяснения упражнений

### Задача 1: Создать функцию, которая принимает два числа и возвращает их сумму

**Пошаговое решение:**
1. Объявляем функцию с именем `sum`
2. Определяем два параметра `a` и `b`
3. В теле функции возвращаем результат сложения `a + b`

```javascript
function sum(a, b) {
    return a + b;
}
```

**Проверка:**
```javascript
console.log(sum(5, 3)); // выведет: 8
console.log(sum(10, -2)); // выведет: 8
```

### Задача 2: Создать функцию, которая принимает имя человека и его возраст и выводит в консоль две строки

**Пошаговое решение:**
1. Объявляем функцию `printPersonInfo`
2. Определяем параметры `name` и `age`
3. Используем шаблонные строки для форматирования вывода
4. Вызываем `console.log` два раза

```javascript
function printPersonInfo(name, age) {
    console.log(`Имя: ${name}`);
    console.log(`Возраст: ${age}`);
}
```

**Проверка:**
```javascript
printPersonInfo('Иван', 30);
// Выведет:
// Имя: Иван
// Возраст: 30
```

### Задача 3: Создать функцию, которая принимает три числа и возвращает самое маленькое из них

**Пошаговое решение:**
1. Объявляем функцию `findMin`
2. Определяем три параметра `a`, `b`, `c`
3. Используем встроенный метод `Math.min` для нахождения минимального значения

```javascript
function findMin(a, b, c) {
    return Math.min(a, b, c);
}
```

**Альтернативное решение (без Math.min):**
```javascript
function findMin(a, b, c) {
    let min = a;
    if (b < min) min = b;
    if (c < min) min = c;
    return min;
}
```

**Проверка:**
```javascript
console.log(findMin(5, 2, 8)); // выведет: 2
console.log(findMin(-1, -5, 0)); // выведет: -5
```

### Задача 4: Создать стрелочную функцию с именем `sum`

**Пошаговое решение:**
1. Объявляем константу `sum`
2. Используем синтаксис стрелочной функции
3. Так как тело функции простое, используем неявный возврат

```javascript
const sum = (a, b) => a + b;
```

**Проверка:**
```javascript
console.log(sum(7, 3)); // выведет: 10
console.log(typeof sum); // выведет: function
```

### Задача 5: Создать анонимную нестрелочную функцию

**Важное примечание:** В JavaScript, когда функция присваивается переменной или константе, она получает имя этой переменной. Для создания действительно анонимной функции нужно передать ее как параметр или использовать в контексте, где она не получает имени.

**Пошаговое решение:**
1. Создаем function expression без имени
2. Передаем ее как параметр в другую функцию или используем в контексте, где она остается анонимной

```javascript
// Пример 1: Передача анонимной функции как колбэка
setTimeout(function() {
    console.log('Это действительно анонимная функция');
}, 1000);

// Пример 2: Использование в обработчике событий
button.addEventListener('click', function() {
    console.log('Анонимная функция-обработчик');
});

// Пример 3: Возврат анонимной функции из другой функции
function createCounter() {
    return function() {
        // Эта функция остается анонимной
        console.log('Счетчик вызван');
    };
}
```

**Если требуется присвоить константе (с учетом того, что функция получит имя):**
```javascript
const anonymousFunc = function() {
    console.log('Функция, присвоенная константе');
    return 'результат';
};
```

**Проверка:**
```javascript
// Для действительно анонимной функции:
setTimeout(function() {
    console.log(this.name); // выведет: "" (пустая строка)
}, 1000);

// Для функции, присвоенной константе:
anonymousFunc(); // выведет: "Функция, присвоенная константе"
console.log(anonymousFunc.name); // выведет: "anonymousFunc" (имя константы)
```

### Задача 6: Создать функцию, которая принимает две функции и возвращает композицию

**Пошаговое решение:**
1. Объявляем функцию `compose`
2. Определяем параметры `f` и `g` (две функции)
3. Возвращаем новую функцию, которая принимает аргумент `x`
4. Внутри новой функции вызываем `f(x)`, затем передаем результат в `g()`
5. Возвращаем результат `g(f(x))`

```javascript
function compose(f, g) {
    return function(x) {
        return g(f(x));
    };
}
```

**Проверка:**
```javascript
const double = x => x * 2;
const addFive = x => x + 5;

const doubleThenAddFive = compose(double, addFive);
console.log(doubleThenAddFive(3)); // выведет: 11 (3*2=6, 6+5=11)
```

### Задача 7: Создать функцию, принимающую объект и возвращающую значение свойства `name`

**Пошаговое решение:**
1. Объявляем функцию `getName`
2. Используем деструктуризацию для извлечения свойства `name` из параметра
3. Возвращаем значение `name`

```javascript
function getName({ name }) {
    return name;
}
```

**Альтернативное решение без деструктуризации:**
```javascript
function getName(obj) {
    return obj.name;
}
```

**Проверка:**
```javascript
const user = { name: 'Алексей', age: 25 };
console.log(getName(user)); // выведет: "Алексей"
```

## Интересные факты о функциях

### Свойства length и name у функций

Каждая функция в JavaScript имеет встроенные свойства:

```javascript
function example(a, b, c) {
    return a + b + c;
}

console.log(example.length); // 3 (количество параметров)
console.log(example.name); // "example" (имя функции)

// Для стрелочных функций:
const arrowFunc = (x, y) => x + y;
console.log(arrowFunc.name); // "arrowFunc"

// Для анонимных функций:
const anonymous = function() {};
console.log(anonymous.name); // "anonymous"
```

### Объявленные по умолчанию arguments и event

#### Объект arguments
В обычных функциях (не стрелочных) доступен объект `arguments`, содержащий все переданные аргументы:

```javascript
function showArguments() {
    console.log(arguments.length); // количество аргументов
    console.log(arguments[0]); // первый аргумент
    console.log(arguments[1]); // второй аргумент
}

showArguments('первый', 'второй', 'третий');
// Выведет:
// 3
// первый
// второй
```

#### Объект event
В обработчиках событий в браузере автоматически передается объект `event`:

```javascript
// В браузере:
button.addEventListener('click', function(event) {
    console.log(event.type); // "click"
    console.log(event.target); // элемент, на котором произошло событие
});
```

## Дополнительные материалы

### Полезные ресурсы для изучения:
- [MDN Web Docs: Функции](https://developer.mozilla.org/ru/docs/Web/JavaScript/Guide/Functions)
- [JavaScript.info: Функции](https://learn.javascript.ru/function-basics)
- [Видео: Функции в JavaScript для начинающих](https://youtube.com/playlist?list=PLqKQF2ojwm3l4oPjsB9chrJmlhZ-zOzWT)

### Практические советы:
- Используйте стрелочные функции для коротких выражений и колбэков
- Применяйте деструктуризацию для работы со сложными параметрами
- Используйте параметры по умолчанию для обеспечения обратной совместимости
- Помните о контексте `this` при работе с методами объектов

### Для дальнейшего изучения:
- Рекурсивные функции
- Замыкания (closures)
- Функции высшего порядка
- Каррирование (currying)
- Генераторы и async/await функции