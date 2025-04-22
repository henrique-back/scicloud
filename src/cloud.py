import matplotlib.pyplot as plt
from wordcloud import WordCloud
import tkinter as tk
from tkinter import filedialog

# Generate the word cloud with higher quality settings
def custom_cloud(words, max_words=40, colormap='viridis', background_color='white', width=1600, height=800, scale=2, ask_to_save=False):
    wordcloud = WordCloud(
        width=width, 
        height=height, 
        background_color=background_color, 
        colormap=colormap,
        max_words=max_words,
        scale=scale
    ).generate_from_frequencies(words)

    # Plot the word cloud
    fig = plt.figure(figsize=(width // 100, height // 100))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # Open a file save dialog if requested
    if ask_to_save:
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG image", "*.png"), ("All Files", "*.*")],
            title="Save Word Cloud As"
        )
        if file_path:
            fig.savefig(file_path, bbox_inches='tight')
            print(f"Word cloud saved to: {file_path}")

    return fig