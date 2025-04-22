import tkinter as tk
from tkinter import filedialog
from nltk.tokenize import word_tokenize

def tokenizer(text):
    tokens = word_tokenize(text)
    combined_tokens = []
    i = 0
    while i < len(tokens):
        if tokens[i] == 'al' and i + 1 < len(tokens) and tokens[i + 1] == '.':
            combined_tokens.append('al.')
            i += 2
        else:
            combined_tokens.append(tokens[i])
            i += 1
    return combined_tokens

def tokenizer_from_dialog():
    # Open file dialog to choose a .txt file
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if not file_path:
        print("No file selected.")
        return None

    # Read and tokenize the file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return tokenizer(text)
