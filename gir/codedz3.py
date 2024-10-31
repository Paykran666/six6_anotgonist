def count_sentences(text):
  """Считает количество предложений в тексте."""
  sentences = text.split(".") # Разделяем текст по точкам
  return len(sentences) # Возвращаем количество полученных предложений

user_text = input("Введите текст: ")
sentence_count = count_sentences(user_text)
print("В тексте", sentence_count, "предложений.")
