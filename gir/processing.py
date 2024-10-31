import re

def is_valid_email(email):
  """Проверяет, является ли строка корректным email-адресом."""
  pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"
  match = re.match(pattern, email)
  return bool(match)

# Примеры использования:
print(is_valid_email("example@test.com")) # True
print(is_valid_email("example@com"))       # False
