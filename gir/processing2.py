import re

def extract_phone_numbers(text):
  """Извлекает все телефонные номера из текста."""
  pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
  phone_numbers = re.findall(pattern, text)
  return phone_numbers

# Пример использования:
text = "My numbers are (123) 456-7890 and 123-456-7890."
print(extract_phone_numbers(text))
# ['(123) 456-7890', '123-456-7890']
