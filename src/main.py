from src.tokenizer import tokenizer_from_dialog
from src.cloud import custom_cloud
from nltk.corpus import stopwords
from collections import Counter
import nltk
import tkinter as tk
from tkinter import simpledialog


nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Prompt for extra stopwords using a simple dialog
def get_additional_stopwords():
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring(
        title="Additional Stopwords",
        prompt="Enter additional stopwords separated by commas (leave blank to skip):"
    )
    if user_input:
        return set(word.strip().lower() for word in user_input.split(','))
    return set()

# Load tokens from file
tokens = tokenizer_from_dialog()

if tokens is None:
    print("No text loaded. Exiting.")
    exit()

# Base and custom stopwords
default_custom_stopwords = set([
    'et', 'al', 'al.', 'fig', 'fig ', 'https', 'sci', 'mar', 'si', 'de', 'figure', 'ch',
    'ais', 'crossref', 'using', 'study', 'used'
])
stop_words = set(stopwords.words('english')).union(default_custom_stopwords)

# Add user-defined stopwords
extra_stopwords = get_additional_stopwords()
stop_words.update(extra_stopwords)

# Clean tokens
filtered_tokens = [
    word.lower()
    for word in tokens
    if len(word) > 1
    and word.lower() not in stop_words
    and not word.isdigit()
    and not (len(word) == 2 and word[1] == '.')
]

# Count and normalize
total_words = len(filtered_tokens)
word_freq = Counter(filtered_tokens)
normalized_freq = {word: count / total_words for word, count in word_freq.items()}

# Take top 100
top_words = dict(Counter(normalized_freq).most_common(100))

# Generate word cloud and prompt to save
custom_cloud(top_words, ask_to_save=True)