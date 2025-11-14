const wordTemplate = "<tr><td>%word</td><td>%description</td></tr>";
const wordListTemplate =
  "<table><thead><tr><th>Word</th><th>Description</th></tr></thead><tbody>%rows</tbody></table>";

export const renderWord = (word) => {
  return wordTemplate
    .replace("%word", word.word)
    .replace("%description", word.description);
};

export const renderWordList = (wordList) => {
  const rows = wordList.words.map(renderWord).join("");
  return wordListTemplate.replace("%rows", rows);
};
