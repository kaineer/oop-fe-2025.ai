# Полный конспект занятия - Объекты в JavaScript

## Введение в объекты

Объекты в JavaScript - это составные структуры данных, которые позволяют хранить коллекции свойств и методов. Они являются основным способом организации данных в JavaScript и используются для моделирования реальных сущностей.

## Способы создания объектов

### Создание объектов как литералов
Самый простой и распространенный способ создания объектов:

```javascript
const person = {
    name: 'Анна',
    age: 25,
    city: 'Москва',
    greet() {
        return `Привет, меня зовут ${this.name}`;
    }
};
```

**Особенности:**
- Простой и читаемый синтаксис
- Подходит для создания единичных объектов
- Не требует дополнительных функций или классов

### Создание объектов через конструкторы
Конструкторы позволяют создавать множество объектов одного типа:

```javascript
function Person(name, age) {
    this.name = name;
    this.age = age;
}

// Добавление методов в прототип
Person.prototype.greet = function() {
    return `Привет, меня зовут ${this.name}`;
};

// Создание экземпляра
const person = new Person('Анна', 25);
```

**Важные моменты:**
- Используйте ключевое слово `new`
- Свойство `__proto__` ссылается на прототип конструктора
- Методы добавляются в `prototype` для экономии памяти

### Использование Object.create()
Создание объектов с указанным прототипом:

```javascript
// Базовый прототип
const personPrototype = {
    greet() {
        return `Привет, меня зовут ${this.name}`;
    },
    introduce() {
        return `Мне ${this.age} лет`;
    }
};

// Создание объекта с указанным прототипом
const person = Object.create(personPrototype);
person.name = 'Анна';
person.age = 25;
```

**Преимущества:**
- Прямой контроль над прототипом
- Гибкость в создании цепочек наследования

### Использование классов
Современный синтаксис для создания объектов и наследования:

```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    greet() {
        return `Привет, меня зовут ${this.name}`;
    }
    
    introduce() {
        return `Мне ${this.age} лет`;
    }
}

// Наследование
class Student extends Person {
    constructor(name, age, grade) {
        super(name, age); // вызов конструктора родителя
        this.grade = grade;
    }
    
    study() {
        return `${this.name} учится в ${this.grade} классе`;
    }
}
```

## Свойства объектов с геттерами и сеттерами

Геттеры и сеттеры - это специальные методы, которые вызываются при чтении и записи свойств:

```javascript
const person = {
    _firstName: 'Анна',
    _lastName: 'Иванова',
    
    // Геттер для полного имени
    get fullName() {
        return `${this._firstName} ${this._lastName}`;
    },
    
    // Сеттер для полного имени
    set fullName(value) {
        const parts = value.split(' ');
        this._firstName = parts[0];
        this._lastName = parts[1] || '';
    },
    
    // Геттер для вычисляемого свойства
    get birthYear() {
        return new Date().getFullYear() - this.age;
    }
};

// Использование
person.fullName = 'Мария Петрова';
console.log(person.fullName); // "Мария Петрова"
console.log(person.birthYear); // вычисляется на основе возраста
```

## Наследование в JavaScript

### Прототипное наследование
JavaScript использует прототипное наследование, где объекты могут наследовать свойства и методы от других объектов:

```javascript
// Базовый объект
const animal = {
    eat() {
        return `${this.name} ест`;
    },
    sleep() {
        return `${this.name} спит`;
    }
};

// Наследование через Object.create()
const dog = Object.create(animal);
dog.name = 'Бобик';
dog.bark = function() {
    return `${this.name} лает`;
};

console.log(dog.eat()); // "Бобик ест"
console.log(dog.bark()); // "Бобик лает"
```

### Наследование через классы
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    
    eat() {
        return `${this.name} ест`;
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
    
    bark() {
        return `${this.name} лает`;
    }
}

const myDog = new Dog('Бобик', 'Овчарка');
console.log(myDog.eat()); // "Бобик ест"
console.log(myDog.bark()); // "Бобик лает"
```

## Пошаговые объяснения упражнений

### Задача 1: Создать пустой объект

**Пошаговое решение:**
1. Используем литерал объекта с пустыми фигурными скобками

```javascript
const emptyObj = {};
```

**Проверка:**
```javascript
console.log(typeof emptyObj); // "object"
console.log(Object.keys(emptyObj).length); // 0
```

### Задача 2: Создать объект с методом getName()

**Пошаговое решение:**
1. Создаем объект с свойством `name`
2. Добавляем метод `getName`, который возвращает `this.name`

```javascript
const person = {
    name: 'Иван',
    getName() {
        return this.name;
    }
};
```

**Проверка:**
```javascript
console.log(person.getName()); // "Иван"
person.name = 'Петр';
console.log(person.getName()); // "Петр"
```

### Задача 3: Создать класс Point с полями x и y

**Пошаговое решение:**
1. Объявляем класс `Point`
2. В конструкторе инициализируем свойства `x` и `y`
3. Используем параметры конструктора для установки значений

```javascript
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}
```

**Проверка:**
```javascript
const point = new Point(5, 10);
console.log(point.x); // 5
console.log(point.y); // 10
```

### Задача 4: Добавить метод move(newX, newY)

**Пошаговое решение:**
1. Добавляем метод `move` в класс `Point`
2. Метод принимает новые координаты
3. Обновляем свойства `x` и `y`

```javascript
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    
    move(newX, newY) {
        this.x = newX;
        this.y = newY;
    }
}
```

**Проверка:**
```javascript
const point = new Point(5, 10);
point.move(15, 20);
console.log(point.x); // 15
console.log(point.y); // 20
```

### Задача 5: Добавить метод moveBy(shiftX, shiftY)

**Пошаговое решение:**
1. Добавляем метод `moveBy` в класс `Point`
2. Метод принимает смещения по осям
3. Увеличиваем текущие координаты на смещения

```javascript
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    
    moveBy(shiftX, shiftY) {
        this.x += shiftX;
        this.y += shiftY;
    }
}
```

**Проверка:**
```javascript
const point = new Point(5, 10);
point.moveBy(3, -2);
console.log(point.x); // 8
console.log(point.y); // 8
```

### Задача 6: Добавить метод mirror(zeroX, zeroY)

**Пошаговое решение:**
1. Добавляем метод `mirror` в класс `Point`
2. Метод принимает координаты центра симметрии
3. Вычисляем симметричные координаты по формуле: `2 * center - coordinate`

```javascript
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    
    mirror(zeroX, zeroY) {
        this.x = 2 * zeroX - this.x;
        this.y = 2 * zeroY - this.y;
    }
}
```

**Проверка:**
```javascript
const point = new Point(5, 10);
point.mirror(0, 0); // отражение относительно начала координат
console.log(point.x); // -5
console.log(point.y); // -10
```

## Интересные факты об объектах

### null это тоже объект

В JavaScript `typeof null` возвращает `"object"`. Это историческая особенность языка:

```javascript
console.log(typeof null); // "object"
console.log(null instanceof Object); // false
```

Это не означает, что `null` является объектом - это примитивное значение. Такое поведение сохраняется для обратной совместимости.

### Производительность прототипирования

Прототипное наследование дает выигрыш в производительности при работе с большим количеством объектов:

```javascript
// Плохо: каждый объект имеет свою копию метода
function createObjectWithMethod() {
    return {
        data: Math.random(),
        method() { return this.data; }
    };
}

// Хорошо: метод находится в прототипе
function PrototypeObject(data) {
    this.data = data;
}
PrototypeObject.prototype.method = function() { return this.data; };

// При 10000+ объектов второй вариант будет быстрее
```

**Практический совет:** Используйте прототипы или классы при создании множества объектов одного типа.

## Дополнительные материалы

### Полезные ресурсы для изучения:
- [MDN Web Docs: Работа с объектами](https://developer.mozilla.org/ru/docs/Web/JavaScript/Guide/Working_with_Objects)
- [JavaScript.info: Объекты](https://learn.javascript.ru/object)
- [Видео: Объекты в JavaScript для начинающих](https://youtube.com/playlist?list=PLqKQF2ojwm3l4oPjsB9chrJmlhZ-zOzWT)

### Практические советы:
- Используйте литералы объектов для простых случаев
- Применяйте классы для сложных структур с наследованием
- Помните о контексте `this` в методах объектов
- Используйте геттеры и сеттеры для вычисляемых свойств

### Для дальнейшего изучения:
- Статические методы и свойства классов
- Приватные поля и методы (синтаксис #)
- Миксины и композиция объектов
- Object.freeze(), Object.seal() для иммутабельности
- Proxy объекты для перехвата операций