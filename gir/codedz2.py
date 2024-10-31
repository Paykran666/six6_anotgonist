def change_reserved_words(text, reserved_words):
  """Изменяет регистр зарезервированных слов в тексте на верхний."""
  words = text.split() # Разделяем текст на слова
  changed_text = []
  for word in words:
    if word.lower() in reserved_words: # Проверяем, есть ли слово в списке зарезервированных
      word = word.upper()
    changed_text.append(word) # Добавляем слово в измененный текст
  return " ".join(changed_text) # Объединяем слова обратно в текст

user_text = input("Введите текст: ")
reserved_words_str = input("Введите зарезервированные слова через пробел: ")
reserved_words = reserved_words_str.split() # Разделяем строку на список слов

changed_text = change_reserved_words(user_text, reserved_words)
print(changed_text)
