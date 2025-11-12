# Краткий конспект занятия - Объекты в JavaScript

## Ключевые концепции

### Создание объектов
- **Литералы объектов** - `const obj = { key: value }`
- **Конструкторы** - `new ObjConstructor()`, свойство `__proto__`
- **Object.create()** - создание объектов с указанным прототипом
- **Классы** - `class`, `extends`, `constructor`, наследование
- **Геттеры и сеттеры** - свойства, вызывающие методы при чтении/записи

### Наследование
- Прототипное наследование через цепочку прототипов
- Наследование на несколько уровней
- Классовое наследование через `extends`

## Примеры для демонстрации

### Создание объекта как литерала
```javascript
const person = {
    name: 'Анна',
    age: 25,
    greet() {
        return `Привет, я ${this.name}`;
    }
};
```

### Создание объекта через конструктор
```javascript
function Person(name, age) {
    this.name = name;
    this.age = age;
}
Person.prototype.greet = function() {
    return `Привет, я ${this.name}`;
};
const person = new Person('Анна', 25);
```

### Использование Object.create()
```javascript
const prototype = {
    greet() {
        return `Привет, я ${this.name}`;
    }
};
const person = Object.create(prototype);
person.name = 'Анна';
person.age = 25;
```

### Использование классов и наследования
```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    greet() {
        return `Привет, я ${this.name}`;
    }
}

class Student extends Person {
    constructor(name, age, grade) {
        super(name, age);
        this.grade = grade;
    }
}
```

### Объект с геттерами
```javascript
const person = {
    firstName: 'Анна',
    lastName: 'Иванова',
    get fullName() {
        return `${this.firstName} ${this.lastName}`;
    },
    set fullName(value) {
        [this.firstName, this.lastName] = value.split(' ');
    }
};
```

## Интересные факты

- **null это тоже объект** - `typeof null` возвращает `"object"`
- **Производительность прототипирования** - выигрыш заметен при большом количестве объектов (более 10000)

## Вопросы для обсуждения

1. В чем разница между созданием объекта через литерал и через конструктор?
2. Как работает цепочка прототипов?
3. Когда использовать классы, а когда прототипное наследование?
4. Зачем нужны геттеры и сеттеры?
5. Почему `typeof null` возвращает `"object"`?
6. В каких случаях прототипирование дает выигрыш в производительности?

## Типичные ошибки

- Забывание `new` при вызове конструктора
- Потеря контекста `this` в методах объектов
- Неправильное использование прототипов
- Путаница между `__proto__` и `prototype`
- Неправильное наследование в классах (забывание `super()`)

## Практические упражнения

### Задача 1: Создать пустой объект
```javascript
const emptyObj = {};
```

### Задача 2: Создать объект с методом getName()
```javascript
const person = {
    name: 'Иван',
    getName() {
        return this.name;
    }
};
```

### Задача 3: Создать класс Point с полями x и y
```javascript
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}
```

### Задача 4: Добавить метод move(newX, newY)
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

### Задача 5: Добавить метод moveBy(shiftX, shiftY)
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

### Задача 6: Добавить метод mirror(zeroX, zeroY)
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

## Дополнительные вопросы для проверки

- Создайте объект с геттером, который вычисляет возраст на основе даты рождения
- Реализуйте наследование между двумя классами (например, Animal → Dog)
- Создайте объект через Object.create() с несколькими методами в прототипе
- Объясните разницу между `__proto__` и `prototype`
