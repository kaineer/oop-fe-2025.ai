import { Word } from "./word.js";

export class WordList {
  constructor() {
    this.words = [];
  }

  addWord(word, description) {
    this.words.push(new Word(word, description));
  }
}
