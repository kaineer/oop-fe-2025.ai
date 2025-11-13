// REF: import
import { renderWordList } from "./renderers.js";
import "./style.css";

import { WordList } from "./word-list.js";

document.querySelector("#app").innerHTML = `
  <div>
    <h1>Crossword</h1>
    <div id="word-list"></div>
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

// REF: render
document.querySelector("#word-list").innerHTML = renderWordList(wordList);
