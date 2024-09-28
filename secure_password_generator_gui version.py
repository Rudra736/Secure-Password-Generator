import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, has_uppercase, has_numbers, has_symbols):
    characters = string.ascii_lowercase
    if has_uppercase:
        characters += string.ascii_uppercase
    if has_numbers:
        characters += string.digits
    if has_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Secure Password Generator")

        # Create input fields
        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0)
        self.length_entry = tk.Entry(master, width=10)
        self.length_entry.grid(row=0, column=1)

        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbox = tk.Checkbutton(master, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_checkbox.grid(row=1, column=0)

        self.numbers_var = tk.IntVar()
        self.numbers_checkbox = tk.Checkbutton(master, text="Include Numbers", variable=self.numbers_var)
        self.numbers_checkbox.grid(row=2, column=0)

        self.symbols_var = tk.IntVar()
        self.symbols_checkbox = tk.Checkbutton(master, text="Include Symbols", variable=self.symbols_var)
        self.symbols_checkbox.grid(row=3, column=0)

        # Create generate button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2)

        # Create password display field
        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.grid(row=5, column=0)
        self.password_entry = tk.Entry(master, width=30)
        self.password_entry.grid(row=5, column=1)

        # Create copy to clipboard button
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=6, column=0, columnspan=2)

    def generate_password(self):
        length = int(self.length_entry.get())
        has_uppercase = self.uppercase_var.get() == 1
        has_numbers = self.numbers_var.get() == 1
        has_symbols = self.symbols_var.get() == 1

        password = generate_password(length, has_uppercase, has_numbers, has_symbols)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        self.master.clipboard_clear()
        self.master.clipboard_append(password)
        messagebox.showinfo("Copied!", "Password copied to clipboard!")

root = tk.Tk()
my_gui = PasswordGeneratorGUI(root)
root.mainloop()