import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if data == "":
        messagebox.showwarning("Warning", "Please enter some data to generate QR.")
        return

    # Generate QR code
    qr = qrcode.make(data)
    qr.save("my_qr.png")

    # Display QR in GUI
    img = Image.open("my_qr.png")
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x400")
root.resizable(False, False)

tk.Label(root, text="Enter text or link:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=5)

tk.Button(root, text="Generate QR", font=("Arial", 12), command=generate_qr).pack(pady=10)

qr_label = tk.Label(root, bg="white", width=200, height=200)
qr_label.pack(pady=10)

root.mainloop()
