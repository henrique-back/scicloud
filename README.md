# 🧠 SciCloud

**SciCloud** is a simple Python tool to tokenize text documents, clean and normalize the tokens, and generate high-resolution word clouds based on word frequencies. It's built with `NLTK`, `matplotlib`, and `wordcloud`, and features a GUI file dialog for loading text files and saving the output.

---

## 📦 Features

- Word frequency analysis
- Customizable word clouds
- Interactive file selection for both input and output
- Tokenize text using NLTK, with special handling for common patterns like `al.`
- Custom and standard stopword removal

---

## 🚀 Quick Start

### 1. Install package
In the terminal, run pip install .

### 2. Create .txt file
SciCloud will read a .txt file containing the text to be processed. This is usually a compilation of abstracts from scientific publications, but could be any kind of text.
To do this, simply create a new .txt file in the docs folder. Then, copy and paste all the texts you wish to include.
SciCloud will treat everything as a single document, so don't worry about indicating where one abstract finishes and the other starts.

### 3. Run main.py
In the terminal, run python main.py

You'll be prompted to choose a .txt file. After processing, a word cloud will be displayed, and you'll be prompted to save it.



