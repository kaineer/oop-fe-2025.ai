# Полный конспект занятия - Объектная модель браузера

## Теория с примерами

### Введение в DOM (Document Object Model)

DOM (Document Object Model) - это программный интерфейс для HTML и XML документов. Он представляет структуру документа в виде дерева объектов, которые можно программно изменять, добавлять или удалять.

### Основные объекты браузера

#### window
Глобальный объект, представляющий окно браузера:

```javascript
// Размеры окна
console.log(window.innerWidth);  // ширина области просмотра
console.log(window.innerHeight); // высота области просмотра

// Навигация
window.location.href = 'https://example.com'; // переход на другую страницу
console.log(window.navigator.userAgent); // информация о браузере
```

#### document
Объект, представляющий загруженную веб-страницу:

```javascript
// Свойства документа
console.log(document.title);      // заголовок страницы
console.log(document.URL);        // URL страницы
console.log(document.doctype);    // тип документа

// Методы для работы с DOM
const body = document.body;       // элемент body
const head = document.head;       // элемент head
```

#### navigator
Объект, содержащий информацию о браузере и операционной системе:

```javascript
console.log(navigator.userAgent);     // строка User-Agent
console.log(navigator.language);      // язык браузера
console.log(navigator.platform);      // платформа (ОС)
console.log(navigator.onLine);        // статус подключения к интернету
```

### Поиск элементов в DOM

#### querySelector и querySelectorAll
Современные методы для поиска элементов по CSS-селекторам:

```javascript
// Поиск первого элемента
const firstButton = document.querySelector('button');
const specificElement = document.querySelector('#unique-id');
const elementByClass = document.querySelector('.my-class');

// Поиск всех элементов
const allButtons = document.querySelectorAll('button');
const allItems = document.querySelectorAll('.item');
const complexSelector = document.querySelectorAll('div.container > p:first-child');
```

#### Традиционные методы поиска
```javascript
// По id
const byId = document.getElementById('my-id');

// По классу (возвращает HTMLCollection)
const byClass = document.getElementsByClassName('my-class');

// По тегу (возвращает HTMLCollection)
const byTag = document.getElementsByTagName('div');
```

#### Навигация по DOM
```javascript
const element = document.querySelector('.target');

// Родительские элементы
const parent = element.parentElement;
const closestParent = element.closest('.container');

// Дочерние элементы
const children = element.children;           // только элементы
const allChildren = element.childNodes;      // все узлы (включая текст)

// Соседние элементы
const nextSibling = element.nextElementSibling;
const prevSibling = element.previousElementSibling;
```

### Работа с классами и атрибутами

#### classList vs className
```javascript
const element = document.querySelector('.my-element');

// className - строка со всеми классами
element.className = 'new-class'; // заменяет все классы
element.className += ' additional-class'; // добавляет класс

// classList - объект для управления классами
element.classList.add('active');           // добавить класс
element.classList.remove('inactive');      // удалить класс
element.classList.toggle('hidden');        // переключить класс
element.classList.contains('visible');     // проверить наличие класса
element.classList.replace('old', 'new');   // заменить класс
```

#### dataset - работа с data-атрибутами
```javascript
// HTML: <div data-user-id="123" data-role="admin"></div>
const element = document.querySelector('div');

// Чтение data-атрибутов
const userId = element.dataset.userId;    // "123"
const role = element.dataset.role;        // "admin"

// Запись data-атрибутов
element.dataset.status = 'active';
element.dataset.customValue = 'hello';
```

### Модификация DOM

#### Добавление элементов
```javascript
const container = document.querySelector('.container');

// append - добавляет элементы или текст
const newDiv = document.createElement('div');
newDiv.textContent = 'Новый элемент';
container.append(newDiv);

// append vs innerHTML
container.innerHTML = '<div>Новый контент</div>'; // заменяет весь HTML
container.append(newDiv); // добавляет к существующему
```

#### Удаление элементов
```javascript
const element = document.querySelector('.to-remove');

// Современный способ
element.remove();

// Старый способ (для совместимости)
if (element.parentNode) {
    element.parentNode.removeChild(element);
}
```

#### Изменение стилей
```javascript
const element = document.querySelector('.styled-element');

// Прямое изменение стилей
element.style.color = 'red';
element.style.backgroundColor = '#f0f0f0';
element.style.fontSize = '16px';
element.style.display = 'none';

// Изменение нескольких стилей через cssText
element.style.cssText = 'color: blue; font-size: 20px; margin: 10px;';
```

## Пошаговые объяснения упражнений

### Задача 1: Получаем ссылку на элемент в списке

**Пошаговое решение:**
1. Находим список на странице
2. Используем querySelector для поиска первого элемента списка
3. Можно использовать различные селекторы в зависимости от структуры

```javascript
// HTML: <ul><li>Первый</li><li>Второй</li><li>Третий</li></ul>

// Первый элемент списка
const firstItem = document.querySelector('ul li:first-child');

// Любой элемент списка по индексу
const secondItem = document.querySelector('ul li:nth-child(2)');

// Элемент по классу
const specialItem = document.querySelector('ul li.special');
```

**Проверка:**
```javascript
console.log(firstItem.textContent); // "Первый"
console.log(firstItem.tagName);     // "LI"
```

### Задача 2: Получаем ссылку на все элементы списка

**Пошаговое решение:**
1. Используем querySelectorAll для поиска всех элементов
2. Получаем NodeList, который можно перебирать

```javascript
// HTML: <ul><li>Первый</li><li>Второй</li><li>Третий</li></ul>

const allItems = document.querySelectorAll('ul li');
```

**Работа с результатом:**
```javascript
// Перебор элементов
allItems.forEach((item, index) => {
    console.log(`Элемент ${index}: ${item.textContent}`);
});

// Преобразование в массив
const itemsArray = Array.from(allItems);

// Количество элементов
console.log(`Всего элементов: ${allItems.length}`);
```

### Задача 3: Получаем ссылку на tr если есть ссылка на td

**Пошаговое решение:**
1. Имеем ссылку на ячейку таблицы (td)
2. Используем closest для поиска ближайшей строки таблицы
3. Альтернативно можно использовать parentElement

```javascript
// HTML: <table><tr><td>Ячейка</td></tr></table>

const td = document.querySelector('td');

// Способ 1: через closest (рекомендуется)
const tr1 = td.closest('tr');

// Способ 2: через parentElement
const tr2 = td.parentElement;

// Способ 3: через parentNode (устаревший)
const tr3 = td.parentNode;
```

**Проверка:**
```javascript
console.log(tr1.tagName); // "TR"
console.log(tr1 === tr2); // true
```

### Задача 4: Считаем количество дочерних элементов

**Пошаговое решение:**
1. Находим контейнерный элемент
2. Используем свойство children для получения дочерних элементов
3. Свойство length возвращает количество элементов

```javascript
// HTML: <div class="container"><p>1</p><p>2</p><span>3</span></div>

const container = document.querySelector('.container');
const childCount = container.children.length;
```

**Дополнительные варианты:**
```javascript
// Только определенные типы элементов
const paragraphCount = container.querySelectorAll('p').length;

// Все дочерние узлы (включая текстовые)
const allNodesCount = container.childNodes.length;

// Фильтрация по классу
const activeChildren = Array.from(container.children)
    .filter(child => child.classList.contains('active')).length;
```

**Проверка:**
```javascript
console.log(`Количество дочерних элементов: ${childCount}`); // 3
```

## Интересные факты о DOM

### jQuery и современный JavaScript

jQuery, когда-то бывшая незаменимой библиотекой для работы с DOM, собирается выпустить 4ю версию. Однако современный JavaScript уже предоставляет аналогичные возможности:

```javascript
// jQuery vs Vanilla JavaScript

// Поиск элементов
$('.my-class') vs document.querySelectorAll('.my-class')

// Добавление класса
$el.addClass('active') vs el.classList.add('active')

// Обработка событий
$el.on('click', handler) vs el.addEventListener('click', handler)

// AJAX запросы
$.ajax() vs fetch()
```

### Особенности NodeList и HTMLCollection

- **NodeList** (возвращается querySelectorAll) - "живая" или "статическая" коллекция
- **HTMLCollection** (возвращается getElementsByClassName) - всегда "живая" коллекция

```javascript
const nodeList = document.querySelectorAll('div');
const htmlCollection = document.getElementsByClassName('item');

// Добавляем новый элемент
const newDiv = document.createElement('div');
newDiv.className = 'item';
document.body.append(newDiv);

console.log(nodeList.length);     // не изменится (статическая)
console.log(htmlCollection.length); // увеличится (живая)
```

## Дополнительные материалы

### Полезные ресурсы для изучения:
- [MDN Web Docs: Document Object Model](https://developer.mozilla.org/ru/docs/Web/API/Document_Object_Model)
- [JavaScript.info: DOM](https://learn.javascript.ru/dom-nodes)
- [Видео: Работа с DOM в JavaScript](https://youtube.com/playlist?list=PLqKQF2ojwm3l4oPjsB9chrJmlhZ-zOzWT)

### Практические советы:
- Всегда проверяйте результат поиска элементов на null
- Используйте современные методы (querySelector, classList, remove)
- Избегайте innerHTML для простых операций
- Используйте data-атрибуты для хранения пользовательских данных
- Оптимизируйте поиск элементов (кешируйте ссылки)

### Для дальнейшего изучения:
- События DOM (addEventListener, event delegation)
- Анимации и переходы через JavaScript
- Работа с формами и валидация
- Web Components и Shadow DOM
- Performance optimization (Virtual DOM, debouncing)