import re

def replace_dates(text):
  """Заменяет даты в тексте из формата DD/MM/YYYY на формат YYYY-MM-DD."""
  pattern = r"(\d{2})/(\d{2})/(\d{4})"
  return re.sub(pattern, r"\3-\2-\1", text)

# Пример использования:
text = "Today's date is 24/10/2024."
print(replace_dates(text)) # "Today's date is 2024-10-24."
