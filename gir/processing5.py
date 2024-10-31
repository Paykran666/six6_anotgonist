import re

def extract_hashtags(text):
  """Находит все хэштеги в тексте."""
  pattern = r"#(\w+)"
  hashtags = re.findall(pattern, text)
  return hashtags

# Пример использования:
text = "Loving the weather! #sunny #beautifulDay #nature"
print(extract_hashtags(text)) # ['sunny', 'beautifulDay', 'nature']
