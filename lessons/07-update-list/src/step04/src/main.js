import { renderWordList } from "./renderers.js";
import { attachHandlers } from "./handlers.js";
import "./style.css";

import { WordList } from "./word-list.js";

document.querySelector("#app").innerHTML = `
  <div>
    <h1>Crossword</h1>
    <div id="word-list"></div>
    <!-- REF: word-form -->
    <div id="word-form">
      <input name="word" type="text" placeholder="Word" />
      <input name="description" type="text" placeholder="Description" />
      <button type="button">Save</button>
    </div>
    <!-- ENDREF -->
  </div>
`;

const wordList = new WordList();
wordList.addWord("класс", "описание того, как должен работать объект");
wordList.addWord(
  "объект",
  "часть программы, которая, в теории, должна уметь работать самостоятельно",
);
wordList.addWord("функция", "блок кода, выполняющий определенную задачу");
wordList.addWord("алгоритм", "последовательность шагов для решения задачи");

const wordListEl = document.querySelector("#word-list");
wordListEl.innerHTML = renderWordList(wordList);
attachHandlers(wordListEl, { wordList, renderWordList });
