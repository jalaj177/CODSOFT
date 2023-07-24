import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Inventor")
        self.geometry("400x300")

        self.length_label = tk.Label(
            self, text="Please specify the desired length for your password:")
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(self)
        self.length_entry.pack(pady=5)

        self.lowercase_var = tk.IntVar()
        self.lowercase_checkbox = tk.Checkbutton(
            self, text="Lowercase Letters (a-z)", variable=self.lowercase_var, bg="lightblue")
        self.lowercase_checkbox.pack()

        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbox = tk.Checkbutton(
            self, text="Uppercase Letters (A-Z)", variable=self.uppercase_var, bg="lightgreen")
        self.uppercase_checkbox.pack()

        self.digits_var = tk.IntVar()
        self.digits_checkbox = tk.Checkbutton(
            self, text="Numerals (0-9)", variable=self.digits_var, bg="lightyellow")
        self.digits_checkbox.pack()

        self.special_var = tk.IntVar()
        self.special_checkbox = tk.Checkbutton(
            self, text="Special Characters (!@#$%^&*)", variable=self.special_var, bg="lightpink")
        self.special_checkbox.pack()

        self.generate_button = tk.Button(
            self, text="Generate Password", command=self.generate_password, bg="orange", fg="white")
        self.generate_button.pack(pady=5)

        self.password_label = tk.Label(
            self, text="", wraplength=350, justify="center", font=("Helvetica", 12))
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter a valid number for password length.")
            return

        if password_length <= 0:
            messagebox.showerror(
                "Error", "Password length must be greater than zero.")
            return

        selected_characters = ""
        if self.lowercase_var.get():
            selected_characters += string.ascii_lowercase
        if self.uppercase_var.get():
            selected_characters += string.ascii_uppercase
        if self.digits_var.get():
            selected_characters += string.digits
        if self.special_var.get():
            selected_characters += string.punctuation

        if not selected_characters:
            messagebox.showerror(
                "Error", "Please select at least one character set.")
            return

        generated_password = ''.join(random.choice(
            selected_characters) for _ in range(password_length))
        self.password_label.config(text=generated_password)


if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
