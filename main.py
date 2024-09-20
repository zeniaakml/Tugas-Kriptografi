import numpy as np
# main.py

import tkinter as tk
from tkinter import filedialog, messagebox
from chipers import (
    vigenere_encrypt, vigenere_decrypt,
    playfair_encrypt, playfair_decrypt,
    hill_encrypt, hill_decrypt
)

class ChiperApp:
    def __init__(self, root):  # Perbaikan di sini (seharusnya __init__)
        self.root = root
        self.root.title("Cipher Encryption Tool")
        self.root.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.text_label = tk.Label(self.root, text="Enter text or upload file:")
        self.text_label.pack()

        self.text_input = tk.Text(self.root, height=5, width=50)
        self.text_input.pack()

        self.key_label = tk.Label(self.root, text="Enter key (min 12 characters):")
        self.key_label.pack()

        self.key_input = tk.Entry(self.root, width=50)
        self.key_input.pack()

        self.cipher_label = tk.Label(self.root, text="Select Cipher Method:")
        self.cipher_label.pack()

        self.cipher_option = tk.StringVar(self.root)
        self.cipher_option.set("Vigenere")  # Default option
        self.cipher_menu = tk.OptionMenu(self.root, self.cipher_option, "Vigenere", "Playfair", "Hill")
        self.cipher_menu.pack()

        self.upload_button = tk.Button(self.root, text="Upload File", command=self.upload_file)
        self.upload_button.pack()

        self.encrypt_button = tk.Button(self.root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(self.root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack()

        self.output_label = tk.Label(self.root, text="Output:")
        self.output_label.pack()

        self.output_text = tk.Text(self.root, height=5, width=50)
        self.output_text.pack()

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_input.delete(1.0, tk.END)
                self.text_input.insert(tk.END, file.read())

    def encrypt_text(self):
        key = self.key_input.get()
        if len(key) < 12:
            messagebox.showwarning("Invalid Key", "Key must be at least 12 characters long.")
            return

        plain_text = self.text_input.get(1.0, tk.END).strip()
        cipher_method = self.cipher_option.get()

        if cipher_method == "Vigenere":
            result = vigenere_encrypt(plain_text, key)
        elif cipher_method == "Playfair":
            result = playfair_encrypt(plain_text, key)
        elif cipher_method == "Hill":
            result = hill_encrypt(plain_text, key)

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

    def decrypt_text(self):
        key = self.key_input.get()
        if len(key) < 12:
            messagebox.showwarning("Invalid Key", "Key must be at least 12 characters long.")
            return

        cipher_text = self.text_input.get(1.0, tk.END).strip()
        cipher_method = self.cipher_option.get()

        if cipher_method == "Vigenere":
            result = vigenere_decrypt(cipher_text, key)
        elif cipher_method == "Playfair":
            result = playfair_decrypt(cipher_text, key)
        elif cipher_method == "Hill":
            result = hill_decrypt(cipher_text, key)

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)

if __name__ == "__main__":  # Perbaikan di sini (seharusnya __name__ dan __main__)
    root = tk.Tk()
    app = ChiperApp(root)
    root.mainloop()
