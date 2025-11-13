// REF: declare
export const attachHandlers = (container, { wordList, renderWordList }) => {
  // ENDREF
  if (container) {
    // REF: remove-button
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
    // ENDREF
  }
};
