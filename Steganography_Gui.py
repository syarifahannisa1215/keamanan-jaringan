from stegano import lsb
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os


class SteganographyApp:
    def __init__(self, root):  # Perbaikan penulisan method __init__
        self.root = root
        self.root.title("Steganography Tool")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Gaya aplikasi dengan warna pastel lembut
        style = ttk.Style()
        style.configure("TFrame", background="#e6f7ff")  # Latar belakang biru pastel lembut
        style.configure("TLabel", background="#e6f7ff", font=("Arial", 14))  # Label
        style.configure(
            "TButton", font=("Arial", 12), padding=5
        )  # Tombol akan diubah dengan manual konfigurasi

        # Header
        self.header_frame = ttk.Frame(self.root, style="TFrame")
        self.header_frame.pack(pady=20)

        self.title_label = tk.Label(
            self.header_frame,
            text="Steganography Tool",
            font=("Arial", 24, "bold"),
            bg="#cce7ff",  # Biru pastel cerah
            fg="#4d4d4d",  # Teks abu-abu gelap
            padx=10,
            pady=10,
        )
        self.title_label.pack()

        # Main frame
        self.main_frame = ttk.Frame(self.root, style="TFrame")
        self.main_frame.pack(pady=30)

        self.hide_button = tk.Button(
            self.main_frame,
            text="Sembunyikan Pesan",
            command=self.hide_message,
            width=25,
            bg="#ffecb3",  # Kuning pastel lembut
            fg="#4d4d4d",  # Teks abu-abu gelap
            font=("Arial", 12),
        )
        self.hide_button.grid(row=0, column=0, padx=10, pady=10)

        self.reveal_button = tk.Button(
            self.main_frame,
            text="Tampilkan Pesan",
            command=self.reveal_message,
            width=25,
            bg="#d1ffd6",  # Hijau pastel lembut
            fg="#4d4d4d",  # Teks abu-abu gelap
            font=("Arial", 12),
        )
        self.reveal_button.grid(row=1, column=0, padx=10, pady=10)

        self.exit_button = tk.Button(
            self.main_frame,
            text="Keluar",
            command=self.root.quit,
            width=25,
            bg="#f4c2c2",  # Merah muda pastel lembut
            fg="#4d4d4d",  # Teks abu-abu gelap
            font=("Arial", 12),
        )
        self.exit_button.grid(row=2, column=0, padx=10, pady=10)

        # Footer
        self.footer_label = tk.Label(
            self.root,
            text="Steganography_Gui",
            font=("Arial", 10),
            bg="#f2f2f2",  # Abu-abu terang
            fg="#4d4d4d",  # Teks abu-abu gelap
            pady=10,
        )
        self.footer_label.pack(side="bottom")

    def hide_message(self):
        # Menyembunyikan pesan
        img_path = filedialog.askopenfilename(
            title="Pilih Gambar",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")],
        )
        if not img_path:
            return

        message = tk.simpledialog.askstring("Masukkan Pesan", "Masukkan pesan yang ingin disembunyikan:")
        if not message:
            return

        save_path = filedialog.asksaveasfilename(
            title="Simpan Gambar",
            defaultextension=".png",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")],
        )
        if not save_path:
            return

        try:
            secret = lsb.hide(img_path, message)
            secret.save(save_path)
            messagebox.showinfo("Berhasil", f"Gambar berhasil disimpan di {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyembunyikan pesan: {e}")

    def reveal_message(self):
        # Menampilkan pesan
        img_path = filedialog.askopenfilename(
            title="Pilih Gambar",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")],
        )
        if not img_path:
            return

        try:
            clear_message = lsb.reveal(img_path)
            if clear_message:
                messagebox.showinfo("Pesan Tersembunyi", f"Pesan: {clear_message}")
            else:
                messagebox.showinfo("Tidak Ada Pesan", "Tidak ada pesan tersembunyi dalam gambar.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membaca gambar: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
