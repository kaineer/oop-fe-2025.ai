// REF: word-template
const wordTemplate =
  "<tr><td>%word</td><td>%description</td><td class='remove-button'>×</td></tr>";
// ENDREF
const wordListTemplate =
  "<table><thead><tr><th>Word</th><th>Description</th></tr></thead><tbody>%rows</tbody></table>";

export const renderWord = (word) => {
  return wordTemplate
    .replace("%word", word.word)
    .replace("%description", word.description);
};

export const renderWordList = (words) => {
  const rows = words.map(renderWord).join("");
  return wordListTemplate.replace("%rows", rows);
};
