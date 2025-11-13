const wordTemplate = "<tr><td>%word</td><td>%description</td></tr>";
const wordListTemplate =
  "<table><thead><tr><th>Word</th><th>Description</th></tr></thead><tbody>%rows</tbody></table>";

// REF: renderWord
export const renderWord = (word) => {
  return wordTemplate
    .replace("%word", word.word)
    .replace("%description", word.description);
};
// ENDREF

// REF: renderWordList
export const renderWordList = (wordList) => {
  const rows = wordList.words.map(renderWord).join("");
  return wordListTemplate.replace("%rows", rows);
};
// ENDREF
