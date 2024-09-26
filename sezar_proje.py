import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title("Crypter")
root.geometry("225x200")

taban = tk.Entry(root)
us = tk.Entry(root)
bilgilendirme = tk.Label(root, text="1. Kutucuğa Taban\n2. Kutucuğa Üs Girin.")
taban.pack()
us.pack()
bilgilendirme.pack()
taban_degeri = ""
us_degeri = ""

def txt_sec():
    global dosya_adi2
    dosya_adi2 = filedialog.askopenfilename(title="Dosya Seç")

def dosyayi_coz():

    with open(dosya_adi2, "r") as file:
        icerik = file.read()

    for i in range(len(icerik)):
        if ord(icerik[i]) > 127:
            messagebox.showerror("Crypt Edilemedi","Dosyada Türkçe Karakterler Bulunuyor!")
            return

    decrypt_icerik = ""
    for i in range(len(icerik)):
        karakter = icerik[i]
        if karakter.isalpha():
            decifre_karakter = chr(ord(karakter) + (int(taban.get())**int(us.get())))
        else:
            decifre_karakter = karakter
        decrypt_icerik += decifre_karakter

    with open(f"{dosya_adi2}_crypted.txt", "w") as file:
        file.write(decrypt_icerik)

    messagebox.showinfo("Crypt Başarılı","Dosya Başarıyla Şifrelendi!")


def decrypt_et():

    with open(dosya_adi2, "r") as file:
        icerik2 = file.read()

    for i in range(len(icerik2)):
        if ord(icerik2[i]) > 127:
            messagebox.showerror("Decrypt Edilemedi","Dosyada Türkçe Karakterler Bulunuyor!")
            return

    decrypt_icerik2 = ""
    for i in range(len(icerik2)):
        karakter2 = icerik2[i]
        if karakter2.isalpha():
            decifre_karakter2 = chr(ord(karakter2) - (int(taban.get())**int(us.get())))
        else:
            decifre_karakter2 = karakter2
        decrypt_icerik2 += decifre_karakter2

    with open(f"{dosya_adi2}_decrypted.txt", "w") as file:
        file.write(decrypt_icerik2)

    messagebox.showinfo("Decrypt Başarılı","Dosya Başarıyla Decrypt Edildi!")

btn_sec = tk.Button(root, text="Dosya Seç", command=txt_sec)
btn_decrypt = tk.Button(root, text="Crypt", command=dosyayi_coz)
btn_dosyayi_coz = tk.Button(root, text="Decrypt", command=decrypt_et)

btn_sec.pack()
btn_decrypt.pack()
btn_dosyayi_coz.pack()

btn_sec.config(command=txt_sec)
btn_decrypt.config(command=dosyayi_coz)
btn_dosyayi_coz.config(command=decrypt_et)

root.mainloop()
