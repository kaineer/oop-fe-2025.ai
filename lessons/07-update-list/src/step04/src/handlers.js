export const attachHandlers = (container, { wordList, renderWordList }) => {
  if (container) {
    container.addEventListener("click", (e) => {
      const target = e.target;
      if (target && target.classList.contains("remove-button")) {
        const row = target.closest("tr");
        const nameCell = row.querySelector("td");
        const word = nameCell.textContent;
        wordList.removeWord(word);
        container.innerHTML = renderWordList(wordList);
      }
    });
  }
};
