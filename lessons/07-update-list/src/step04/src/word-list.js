import { Word } from "./word.js";

export class WordList {
  constructor() {
    this.words = [];
  }

  addWord(word, description) {
    this.words.push(new Word(word, description));
  }

  removeWord(_word) {
    this.words = this.words.filter(({ word }) => word !== _word);
  }

  updateWord(_word, description) {
    const wordToUpdate = this.words.find(({ word }) => word === _word);
    wordToUpdate.description = description;
  }
}
