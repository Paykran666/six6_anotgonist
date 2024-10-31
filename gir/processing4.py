def remove_duplicate_words(text):
  """Удаляет повторяющиеся подряд идущие слова в строке."""
  words = text.split()
  result = []
  previous_word = None
  for word in words:
    if word != previous_word:
      result.append(word)
      previous_word = word
  return " ".join(result)

# Пример использования:
text = "This is is a test test."
print(remove_duplicate_words(text)) # "This is a test."
