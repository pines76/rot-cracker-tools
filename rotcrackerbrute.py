import tkinter as tk
from tkinter import ttk

# English letter frequency (approximate)
LETTER_FREQ = {
    'E': 12.0, 'T': 9.1, 'A': 8.1, 'O': 7.5, 'I': 7.0, 'N': 6.7,
    'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3, 'L': 4.0,
    'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4, 'F': 2.2,
    'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5, 'V': 1.0,
    'K': 0.8, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07
}

def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def score_text(text):
    score = 0
    for char in text.upper():
        score += LETTER_FREQ.get(char, 0)
    return score

def break_cipher():
    encrypted = input_text.get("1.0", tk.END).strip()
    output_box.delete(*output_box.get_children())

    best_score = -1
    best_guess = ""

    for shift in range(26):
        decrypted = caesar_decrypt(encrypted, shift)
        score = score_text(decrypted)

        output_box.insert("", "end", values=(shift, decrypted))

        if score > best_score:
            best_score = score
            best_guess = f"Shift {shift}: {decrypted}"

    best_label.config(text="Best guess: " + best_guess)

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher Breaker")
root.geometry("800x500")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Encrypted Message:").pack(anchor="w")
input_text = tk.Text(frame, height=4)
input_text.pack(fill="x", pady=5)

ttk.Button(frame, text="Break Cipher", command=break_cipher).pack(pady=5)

columns = ("Shift", "Decrypted Text")
output_box = ttk.Treeview(frame, columns=columns, show="headings")
output_box.heading("Shift", text="Shift")
output_box.heading("Decrypted Text", text="Decrypted Text")
output_box.pack(fill="both", expand=True)

best_label = ttk.Label(frame, text="Best guess:")
best_label.pack(pady=5)

root.mainloop()
