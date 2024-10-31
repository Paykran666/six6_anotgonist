def is_palindrome(text):
  """Проверяет, является ли текст палиндромом."""
  text = text.lower().replace(" ", "") # Приводим к нижнему регистру и удаляем пробелы
  return text == text[::-1] # Сравниваем текст с его обратным

user_text = input("Введите строку: ")
if is_palindrome(user_text):
  print("Строка является палиндромом.")
else:
  print("Строка не является палиндромом.")
