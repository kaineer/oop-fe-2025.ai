# Полный конспект занятия - Массивы и работа с ними в JavaScript

## Теория с примерами

### Введение в массивы

Массивы в JavaScript - это упорядоченные коллекции элементов, которые могут содержать данные разных типов. Они являются одним из основных инструментов для работы с наборами данных.

### Создание массивов

#### Создание массива как литерала
Самый простой способ создания массива:

```javascript
// Пустой массив
const emptyArray = [];

// Массив с числами
const numbers = [1, 2, 3, 4, 5];

// Массив со строками
const fruits = ['яблоко', 'банан', 'апельсин'];

// Смешанный массив
const mixed = [1, 'текст', true, null, { name: 'объект' }];
```

#### Получение массива слов из строки
Часто возникает необходимость преобразовать строку в массив:

```javascript
const sentence = "JavaScript это мощный язык программирования";
const words = sentence.split(' ');
// Результат: ['JavaScript', 'это', 'мощный', 'язык', 'программирования']

const csvData = "яблоко,банан,апельсин";
const fruits = csvData.split(',');
// Результат: ['яблоко', 'банан', 'апельсин']
```

#### Получение длины массива
Свойство `length` возвращает количество элементов в массиве:

```javascript
const arr = [10, 20, 30, 40];
console.log(arr.length); // 4
```

### Основные методы массивов

#### forEach - выполнение действия для каждого элемента
Метод `forEach` выполняет указанную функцию один раз для каждого элемента массива:

```javascript
const numbers = [1, 2, 3, 4, 5];

numbers.forEach(function(number, index, array) {
    console.log(`Элемент ${number} имеет индекс ${index}`);
});
// Выведет:
// Элемент 1 имеет индекс 0
// Элемент 2 имеет индекс 1
// Элемент 3 имеет индекс 2
// Элемент 4 имеет индекс 3
// Элемент 5 имеет индекс 4
```

**Три аргумента функции обратного вызова:**
- `element` - текущий обрабатываемый элемент
- `index` - индекс текущего элемента
- `array` - сам массив

#### map - преобразование элементов
Метод `map` создает новый массив с результатами вызова указанной функции для каждого элемента:

```javascript
const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map(function(number) {
    return number * 2;
});
// Результат: [2, 4, 6, 8, 10]

const strings = numbers.map(num => `Число: ${num}`);
// Результат: ['Число: 1', 'Число: 2', 'Число: 3', 'Число: 4', 'Число: 5']
```

#### filter - фильтрация элементов
Метод `filter` создает новый массив со всеми элементами, прошедшими проверку:

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const evenNumbers = numbers.filter(function(number) {
    return number % 2 === 0;
});
// Результат: [2, 4, 6, 8, 10]

const longWords = ['cat', 'elephant', 'dog', 'butterfly'].filter(word => word.length > 3);
// Результат: ['elephant', 'butterfly']
```

#### reduce - агрегация элементов
Метод `reduce` применяет функцию к аккумулятору и каждому элементу массива, сводя его к одному значению:

```javascript
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce(function(accumulator, currentValue) {
    return accumulator + currentValue;
}, 0);
// Результат: 15

const product = numbers.reduce((acc, num) => acc * num, 1);
// Результат: 120
```

### Модификация массивов

#### Добавление и удаление элементов

```javascript
const fruits = ['яблоко', 'банан'];

// Добавление в конец
fruits.push('апельсин'); // ['яблоко', 'банан', 'апельсин']

// Удаление с конца
const lastFruit = fruits.pop(); // 'апельсин', массив: ['яблоко', 'банан']

// Добавление в начало
fruits.unshift('лимон'); // ['лимон', 'яблоко', 'банан']

// Удаление с начала
const firstFruit = fruits.shift(); // 'лимон', массив: ['яблоко', 'банан']
```

### Поиск и сортировка

#### Поиск элементов

```javascript
const numbers = [10, 20, 30, 20, 40];

// indexOf - поиск первого вхождения
console.log(numbers.indexOf(20)); // 1
console.log(numbers.indexOf(50)); // -1 (не найдено)

// lastIndexOf - поиск последнего вхождения
console.log(numbers.lastIndexOf(20)); // 3

// find - поиск по условию
const firstEven = numbers.find(num => num % 2 === 0); // 10

// findIndex - поиск индекса по условию
const firstEvenIndex = numbers.findIndex(num => num % 2 === 0); // 0
```

#### Сортировка

```javascript
const numbers = [40, 10, 30, 20];

// sort() без функции сравнения (сортировка как строк)
numbers.sort(); // [10, 20, 30, 40] - работает для чисел

// Для надежной сортировки чисел
numbers.sort((a, b) => a - b); // по возрастанию
numbers.sort((a, b) => b - a); // по убыванию

const words = ['банан', 'яблоко', 'апельсин'];
words.sort(); // ['апельсин', 'банан', 'яблоко'] - алфавитная сортировка
```

#### Получение части массива (slice)

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// slice(start, end) - end не включается
const firstThree = numbers.slice(0, 3); // [1, 2, 3]
const lastThree = numbers.slice(-3); // [8, 9, 10]
const middle = numbers.slice(3, 7); // [4, 5, 6, 7]
```

### Суммирование цифр числа

```javascript
const number = 12345;

// Преобразование в строку, затем в массив символов, и суммирование
const sumOfDigits = number
    .toString()        // "12345"
    .split('')         // ['1', '2', '3', '4', '5']
    .map(Number)       // [1, 2, 3, 4, 5]
    .reduce((acc, digit) => acc + digit, 0); // 15
```

## Пошаговые объяснения упражнений

### Задача 1: Создать пустой массив

**Пошаговое решение:**
1. Используем литерал массива с пустыми квадратными скобками

```javascript
const emptyArray = [];
```

**Проверка:**
```javascript
console.log(Array.isArray(emptyArray)); // true
console.log(emptyArray.length); // 0
```

### Задача 2: Создать массив 7 дней недели

**Пошаговое решение:**
1. Создаем массив с названиями дней недели в правильном порядке
2. Используем строковые литералы для каждого дня

```javascript
const weekDays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'];
```

**Проверка:**
```javascript
console.log(weekDays.length); // 7
console.log(weekDays[0]); // "понедельник"
console.log(weekDays[6]); // "воскресенье"
```

### Задача 3: Выбрать только выходные дни недели

**Пошаговое решение:**
1. Используем метод `filter` для массива дней недели
2. В функции проверяем, является ли день субботой или воскресеньем

```javascript
const weekends = weekDays.filter(day => day === 'суббота' || day === 'воскресенье');
```

**Альтернативное решение с slice:**
```javascript
const weekends = weekDays.slice(5); // выходные всегда последние два дня
```

**Альтернативное решение с includes:**
```javascript
const weekends = weekDays.filter(day => ['суббота', 'воскресенье'].includes(day));
```

**Проверка:**
```javascript
console.log(weekends); // ['суббота', 'воскресенье']
console.log(weekends.length); // 2

// Проверка для slice решения:
const weekendsSlice = weekDays.slice(5);
console.log(weekendsSlice); // ['суббота', 'воскресенье']
console.log(weekendsSlice.length); // 2
```

### Задача 4: Выбрать только рабочие дни недели

**Пошаговое решение:**
1. Используем метод `filter` для массива дней недели
2. В функции исключаем субботу и воскресенье

```javascript
const workDays = weekDays.filter(day => day !== 'суббота' && day !== 'воскресенье');
```

**Альтернативное решение с slice:**
```javascript
const workDays = weekDays.slice(0, 5); // рабочие дни всегда первые пять
```

**Альтернативное решение с includes:**
```javascript
const workDays = weekDays.filter(day => !['суббота', 'воскресенье'].includes(day));
```

**Проверка:**
```javascript
console.log(workDays); // ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
console.log(workDays.length); // 5

// Проверка для slice решения:
const workDaysSlice = weekDays.slice(0, 5);
console.log(workDaysSlice); // ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
console.log(workDaysSlice.length); // 5
```

### Задача 5: Для массива от 1 до 10 получить массив квадратов чисел

**Пошаговое решение:**
1. Создаем массив чисел от 1 до 10
2. Используем метод `map` для преобразования каждого числа в его квадрат

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const squares = numbers.map(num => num * num);
```

**Проверка:**
```javascript
console.log(squares); // [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
console.log(squares.length); // 10
```

### Задача 6: Для массива от 1 до 10 получить сумму элементов

**Пошаговое решение:**
1. Создаем массив чисел от 1 до 10
2. Используем метод `reduce` для суммирования всех элементов
3. Начальное значение аккумулятора устанавливаем в 0

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const sum = numbers.reduce((acc, num) => acc + num, 0);
```

**Проверка:**
```javascript
console.log(sum); // 55 (1+2+3+4+5+6+7+8+9+10)
```

## Интересные факты о массивах

### Object.keys() возвращает строковые индексы

При использовании `Object.keys()` с массивом, возвращаются строковые представления индексов:

```javascript
const arr = [1, 2, 3];
console.log(Object.keys(arr)); // ['0', '1', '2']
```

Это происходит потому, что массивы в JavaScript являются объектами, а индексы - это свойства объекта.

### sort() vs toSorted()

Метод `sort()` изменяет исходный массив, что может быть неожиданно:

```javascript
const numbers = [3, 1, 4, 1, 5];
const sorted = numbers.sort(); // numbers теперь [1, 1, 3, 4, 5]
```

Современный метод `toSorted()` создает новый отсортированный массив:

```javascript
const numbers = [3, 1, 4, 1, 5];
const sorted = numbers.toSorted(); // [1, 1, 3, 4, 5], numbers остается [3, 1, 4, 1, 5]
```

## Дополнительные материалы

### Полезные ресурсы для изучения:
- [MDN Web Docs: Массивы](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [JavaScript.info: Массивы](https://learn.javascript.ru/array)
- [Видео: Методы массивов в JavaScript](https://youtube.com/playlist?list=PLqKQF2ojwm3l4oPjsB9chrJmlhZ-zOzWT)

### Практические советы:
- Используйте `map` когда нужно преобразовать все элементы
- Используйте `filter` когда нужно отобрать элементы по условию
- Используйте `reduce` для агрегации данных
- Помните, что `forEach` не возвращает новый массив
- Всегда указывайте начальное значение в `reduce`

### Для дальнейшего изучения:
- Методы `some()` и `every()` для проверки условий
- Метод `flat()` для работы с многомерными массивами
- Метод `flatMap()` для комбинации map и flat
- Деструктуризация массивов
- Spread оператор с массивами