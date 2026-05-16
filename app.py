import tkinter as tk
from tkinter import messagebox, scrolledtext

alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar(text, key, mode):
    result = ""

    for char in text:
        lower_char = char.lower()

        if lower_char in alphabet:
            index = alphabet.index(lower_char)

            if mode == "encrypt":
                new_index = (index + key) % 26
            else:
                new_index = (index - key) % 26

            new_char = alphabet[new_index]

            if char.isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += char

    return result


def encrypt_text():
    text = text_input.get("1.0", tk.END).strip()

    if not text:
        messagebox.showerror("Ошибка", "Введите текст")
        return

    key = int(key_input.get())

    encrypted = caesar(text, key, "encrypt")

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"🔒 Зашифрованный текст:\n{encrypted}")


def decrypt_text():
    text = text_input.get("1.0", tk.END).strip()

    if not text:
        messagebox.showerror("Ошибка", "Введите текст")
        return

    key = int(key_input.get())

    decrypted = caesar(text, key, "decrypt")

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"🔓 Расшифрованный текст:\n{decrypted}")


def brute_force():
    text = text_input.get("1.0", tk.END).strip()

    if not text:
        messagebox.showerror("Ошибка", "Введите текст")
        return

    brute_box.delete("1.0", tk.END)

    for key in range(26):
        decrypted = caesar(text, key, "decrypt")
        brute_box.insert(tk.END, f"Ключ {key}: {decrypted}\n\n")


def clear_all():
    text_input.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)
    brute_box.delete("1.0", tk.END)
    key_input.delete(0, tk.END)
    key_input.insert(0, "3")


# Окно
root = tk.Tk()
root.title("Шифр Цезаря")
root.geometry("900x700")
root.configure(bg="#0f172a")

title = tk.Label(
    root,
    text="🔐 Шифр Цезаря",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg="#0f172a"
)
title.pack(pady=15)

# Текст
tk.Label(
    root,
    text="Введите текст",
    fg="white",
    bg="#0f172a",
    font=("Segoe UI", 12)
).pack()

text_input = scrolledtext.ScrolledText(
    root,
    width=80,
    height=6,
    font=("Consolas", 12),
    bg="#111827",
    fg="white",
    insertbackground="white"
)
text_input.pack(pady=10)

# Ключ
tk.Label(
    root,
    text="Ключ (0-25)",
    fg="white",
    bg="#0f172a",
    font=("Segoe UI", 12)
).pack()

key_input = tk.Entry(
    root,
    font=("Segoe UI", 12),
    justify="center"
)
key_input.insert(0, "3")
key_input.pack(pady=10)

# Кнопки
button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack(pady=10)

encrypt_btn = tk.Button(
    button_frame,
    text="🔒 Зашифровать",
    command=encrypt_text,
    bg="#38bdf8",
    fg="black",
    font=("Segoe UI", 11, "bold"),
    width=18
)
encrypt_btn.grid(row=0, column=0, padx=5)

decrypt_btn = tk.Button(
    button_frame,
    text="🔓 Расшифровать",
    command=decrypt_text,
    bg="#818cf8",
    fg="black",
    font=("Segoe UI", 11, "bold"),
    width=18
)
decrypt_btn.grid(row=0, column=1, padx=5)

brute_btn = tk.Button(
    button_frame,
    text="🧠 Брутфорс",
    command=brute_force,
    bg="#22c55e",
    fg="black",
    font=("Segoe UI", 11, "bold"),
    width=18
)
brute_btn.grid(row=1, column=0, pady=10)

clear_btn = tk.Button(
    button_frame,
    text="🧹 Очистить",
    command=clear_all,
    bg="#f97316",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=18
)
clear_btn.grid(row=1, column=1, pady=10)

# Результат
output_box = scrolledtext.ScrolledText(
    root,
    width=80,
    height=5,
    font=("Consolas", 12),
    bg="#111827",
    fg="#93c5fd",
    insertbackground="white"
)
output_box.pack(pady=15)

# Брутфорс
tk.Label(
    root,
    text="Все варианты брутфорса",
    fg="white",
    bg="#0f172a",
    font=("Segoe UI", 13, "bold")
).pack()

brute_box = scrolledtext.ScrolledText(
    root,
    width=80,
    height=12,
    font=("Consolas", 11),
    bg="#111827",
    fg="#dbeafe",
    insertbackground="white"
)
brute_box.pack(pady=10)

root.mainloop()