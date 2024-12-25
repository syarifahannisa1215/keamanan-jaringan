import tkinter as tk
from tkinter import messagebox

class Enigma:
    def __init__(self, rotor1_pos=0, rotor2_pos=0, rotor3_pos=0):
        # Rotor dan reflector
        self.rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        self.rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
        self.rotor3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
        self.reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

        # Posisi awal rotor
        self.rotor1_pos = rotor1_pos
        self.rotor2_pos = rotor2_pos
        self.rotor3_pos = rotor3_pos

        # Rotor invers untuk proses dekripsi
        self.inverse_rotor1 = self.inverse(self.rotor1)
        self.inverse_rotor2 = self.inverse(self.rotor2)
        self.inverse_rotor3 = self.inverse(self.rotor3)

    def inverse(self, rotor):
        """Membuat rotor invers untuk proses dekripsi."""
        inverse_rotor = [0] * 26
        for i in range(26):
            inverse_rotor[rotor[i]] = i
        return inverse_rotor

    def encrypt_decrypt_char(self, ch):
        """Enkripsi atau dekripsi satu karakter."""
        if ch.isalpha():
            is_lower = ch.islower()
            ch = ch.upper()

            # Offset awal
            offset = ord(ch) - ord('A')

            # Rotor maju
            offset = (self.rotor1[(offset + self.rotor1_pos) % 26] - self.rotor1_pos) % 26
            offset = (self.rotor2[(offset + self.rotor2_pos) % 26] - self.rotor2_pos) % 26
            offset = (self.rotor3[(offset + self.rotor3_pos) % 26] - self.rotor3_pos) % 26

            # Reflektor
            offset = self.reflector[offset]

            # Rotor mundur (menggunakan rotor invers)
            offset = (self.inverse_rotor3[(offset + self.rotor3_pos) % 26] - self.rotor3_pos) % 26
            offset = (self.inverse_rotor2[(offset + self.rotor2_pos) % 26] - self.rotor2_pos) % 26
            offset = (self.inverse_rotor1[(offset + self.rotor1_pos) % 26] - self.rotor1_pos) % 26

            # Rotasi rotor setelah setiap karakter
            self.rotor1_pos = (self.rotor1_pos + 1) % 26
            if self.rotor1_pos == 0:
                self.rotor2_pos = (self.rotor2_pos + 1) % 26
                if self.rotor2_pos == 0:
                    self.rotor3_pos = (self.rotor3_pos + 1) % 26

            result = chr(offset + ord('A'))
            return result.lower() if is_lower else result
        else:
            return ch

    def process(self, text):
        """Memproses string untuk enkripsi atau dekripsi."""
        result = ''.join(self.encrypt_decrypt_char(ch) for ch in text)
        return result

# Fungsi untuk enkripsi dan dekripsi teks
def enkripsi():
    text = text_input.get("1.0", tk.END).strip()
    rotor1_pos = int(rotor1_pos_entry.get())
    rotor2_pos = int(rotor2_pos_entry.get())
    rotor3_pos = int(rotor3_pos_entry.get())

    enigma = Enigma(rotor1_pos, rotor2_pos, rotor3_pos)
    encrypted_text = enigma.process(text)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, encrypted_text)

def dekripsi():
    text = text_input.get("1.0", tk.END).strip()
    rotor1_pos = int(rotor1_pos_entry.get())
    rotor2_pos = int(rotor2_pos_entry.get())
    rotor3_pos = int(rotor3_pos_entry.get())

    enigma = Enigma(rotor1_pos, rotor2_pos, rotor3_pos)
    decrypted_text = enigma.process(text)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, decrypted_text)

# Membuat window utama
window = tk.Tk()
window.title("Enigma Cipher")
window.config(bg="#2C3E50")  # Background dark blue

# Membuat elemen GUI
frame = tk.Frame(window, bg="#34495E")  # Background gray-blue
frame.pack(padx=10, pady=10)

# Label dan entry untuk posisi rotor
rotor1_pos_label = tk.Label(frame, text="Posisi Rotor 1:", fg="white", bg="#34495E", font=("Helvetica", 12))
rotor1_pos_label.grid(row=0, column=0, padx=5, pady=5)
rotor1_pos_entry = tk.Entry(frame, font=("Helvetica", 12), bd=2, relief="solid")
rotor1_pos_entry.grid(row=0, column=1, padx=5, pady=5)

rotor2_pos_label = tk.Label(frame, text="Posisi Rotor 2:", fg="white", bg="#34495E", font=("Helvetica", 12))
rotor2_pos_label.grid(row=1, column=0, padx=5, pady=5)
rotor2_pos_entry = tk.Entry(frame, font=("Helvetica", 12), bd=2, relief="solid")
rotor2_pos_entry.grid(row=1, column=1, padx=5, pady=5)

rotor3_pos_label = tk.Label(frame, text="Posisi Rotor 3:", fg="white", bg="#34495E", font=("Helvetica", 12))
rotor3_pos_label.grid(row=2, column=0, padx=5, pady=5)
rotor3_pos_entry = tk.Entry(frame, font=("Helvetica", 12), bd=2, relief="solid")
rotor3_pos_entry.grid(row=2, column=1, padx=5, pady=5)

# Text input untuk memasukkan teks
text_input_label = tk.Label(frame, text="Masukkan Teks:", fg="white", bg="#34495E", font=("Helvetica", 12))
text_input_label.grid(row=3, column=0, padx=5, pady=5)
text_input = tk.Text(frame, height=5, width=40, font=("Helvetica", 12), bd=2, relief="solid")
text_input.grid(row=3, column=1, padx=5, pady=5)

# Tombol untuk enkripsi dan dekripsi
encrypt_button = tk.Button(frame, text="Enkripsi", command=enkripsi, bg="#16A085", fg="white", font=("Helvetica", 12), relief="solid", bd=3)
encrypt_button.grid(row=4, column=0, padx=5, pady=5)

decrypt_button = tk.Button(frame, text="Dekripsi", command=dekripsi, bg="#E74C3C", fg="white", font=("Helvetica", 12), relief="solid", bd=3)
decrypt_button.grid(row=4, column=1, padx=5, pady=5)

# Efek hover pada tombol
def on_enter(event):
    event.widget.config(bg="#1abc9c")

def on_leave(event):
    event.widget.config(bg="#16A085")

encrypt_button.bind("<Enter>", on_enter)
encrypt_button.bind("<Leave>", on_leave)

decrypt_button.bind("<Enter>", on_enter)
decrypt_button.bind("<Leave>", on_leave)

# Output text untuk menampilkan hasil
text_output_label = tk.Label(frame, text="Hasil:", fg="white", bg="#34495E", font=("Helvetica", 12))
text_output_label.grid(row=5, column=0, padx=5, pady=5)
text_output = tk.Text(frame, height=5, width=40, font=("Helvetica", 12), bd=2, relief="solid")
text_output.grid(row=5, column=1, padx=5, pady=5)

# Menjalankan aplikasi
window.mainloop()
