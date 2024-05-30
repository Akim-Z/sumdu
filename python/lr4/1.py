import string

# Початковий текст
text = """
Python is a high-level programming language known for its simplicity and readability. 
It is widely used in various fields such as web development, data analysis, artificial intelligence, 
and automation. Python's syntax is straightforward, making it easy for beginners to learn and 
write code efficiently. The extensive standard library provides numerous modules and functions 
that facilitate different tasks without needing to write code from scratch. Python supports multiple 
programming paradigms, including procedural, object-oriented, and functional programming. 
Its dynamic typing and dynamic binding features offer flexibility and versatility. 
Overall, Python is a powerful language with a vibrant community and excellent documentation, 
making it a top choice for developers worldwide.
"""

# Приведення тексту до нижнього регістру
lower_text = text.lower()

# Розбиття тексту на слова
words = lower_text.split()

# Видалення пунктуації з кожного слова
cleaned_words = [word.strip(string.punctuation) for word in words]

# З'єднання оброблених слів у новий текст
cleaned_text = ' '.join(cleaned_words)

# Виведення початкового та обробленого тексту
print("Початковий текст:")
print(text)
print("\nОброблений текст:")
print(cleaned_text)
