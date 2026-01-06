import tkinter as tk
from tkinter import scrolledtext
from collections import Counter

def decrypt_caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = -shift if char.islower() else -shift
            shifted_char = chr((ord(char) - 97 + shift_amount) % 26 + 97) if char.islower() else chr((ord(char) - 65 + shift_amount) % 26 + 65)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def find_correct_shift(encrypted_text):
    frequency = Counter(encrypted_text.lower())
    most_common_letter_encrypted, _ = frequency.most_common(1)[0]
    
    # Assuming the most common letter in English is 'e'
    assumed_most_common = 'e'
    guessed_shift = (ord(most_common_letter_encrypted) - ord(assumed_most_common)) % 26
    decrypted_message = decrypt_caesar_cipher(encrypted_text, guessed_shift)
    
    return guessed_shift, decrypted_message

def crack_cipher():
    encrypted_text = text_entry.get("1.0", tk.END).strip()
    guessed_shift, message = find_correct_shift(encrypted_text)
    cracked_messages.delete(1.0, tk.END)
    cracked_messages.insert(tk.END, f"Guessed Shift: {guessed_shift}\nDecrypted Message: {message}")


root = tk.Tk()
root.title("Caesar Cipher cracker!")

text_entry = tk.scrolledtext.ScrolledText(root, width=40, height=10)
text_entry.pack(pady=10)

crack_button = tk.Button(root, text="Break", command=crack_cipher)
crack_button.pack(pady=5)

cracked_messages = tk.scrolledtext.ScrolledText(root, width=40, height=5)
cracked_messages.pack(pady=10)


root.mainloop()