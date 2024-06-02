import tkinter as tk
from tkinter import messagebox
import time

# List of sentences for typing
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How razorback-jumping frogs can level six piqued gymnasts!",
    "Sphinx of black quartz, judge my vow.",
    "Two driven jocks help fax my big quiz.",
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.sentence = ""
        self.start_time = 0
        self.end_time = 0
        
        self.sentence_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.sentence_label.pack(pady=20)
        
        self.entry = tk.Entry(root, width=100, font=("Helvetica", 14))
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.check_result)
        
        self.start_button = tk.Button(root, text="Start Test", command=self.start_test, font=("Helvetica", 14))
        self.start_button.pack(pady=20)
        
    def start_test(self):
        self.sentence = sentences.pop(0)  # Get the first sentence from the list
        sentences.append(self.sentence)  # Move the sentence to the end of the list
        self.sentence_label.config(text=self.sentence)
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.start_time = time.time()
        
    def check_result(self, event):
        self.end_time = time.time()
        typed_text = self.entry.get()
        time_taken = self.end_time - self.start_time
        
        # Calculate typing speed (words per minute)
        words_typed = len(typed_text.split())
        words_per_minute = (words_typed / time_taken) * 60
        
        if typed_text == self.sentence:
            messagebox.showinfo("Result", f"Correct!\nTime taken: {time_taken:.2f} seconds\nTyping speed: {words_per_minute:.2f} WPM")
        else:
            messagebox.showinfo("Result", f"Incorrect.\nTime taken: {time_taken:.2f} seconds\nTyping speed: {words_per_minute:.2f} WPM")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
