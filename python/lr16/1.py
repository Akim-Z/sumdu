import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from collections import Counter
import matplotlib.pyplot as plt

# Завантаження тексту
nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

text = gutenberg.raw('austen-persuasion.txt')

# Видалення пунктуації та перетворення на нижній регістр
text = text.translate(str.maketrans('', '', string.punctuation))
text = text.lower()

# Токенізація тексту
words = word_tokenize(text)

# Визначення 10 найбільш вживаних слів до видалення стоп-слів
word_freq_before = Counter(words)
top_10_words_before = word_freq_before.most_common(10)
print("10 найбільш вживаних слів у тексті до видалення стоп-слів:", top_10_words_before)

# Побудова стовпчастої діаграми для топ-10 слів до видалення стоп-слів
words_before, freqs_before = zip(*top_10_words_before)
plt.bar(words_before, freqs_before)
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('10 найбільш вживаних слів у тексті (до видалення стоп-слів)')
plt.xticks(rotation=45)
plt.show()

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
words_without_stopwords = [word for word in words if word not in stop_words]

# Визначення 10 найбільш вживаних слів після видалення стоп-слів
word_freq_after = Counter(words_without_stopwords)
top_10_words_after = word_freq_after.most_common(10)
print("10 найбільш вживаних слів у тексті після видалення стоп-слів:", top_10_words_after)

# Побудова стовпчастої діаграми після видалення стоп-слів
words_after, freqs_after = zip(*top_10_words_after)
plt.bar(words_after, freqs_after)
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('10 найбільш вживаних слів у тексті (після видалення стоп-слів)')
plt.xticks(rotation=45)
plt.show()
