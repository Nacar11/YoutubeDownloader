# pip install customtkinter

import customtkinter
import ytDownloader
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root  = customtkinter.CTk()
root.geometry("500x300")

def download():
    print("test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Youtube Downloader", text_color="blue")
label.pack(pady=12, padx=20)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Place Link Here")
entry1.pack(pady=12, padx=20)

button = customtkinter.CTkButton(master=frame, text="Preview", command=download)
button.pack(pady=12, padx=20)

button = customtkinter.CTkButton(master=frame, text="Download", command=download)
button.pack(pady=12, padx=20)

root.mainloop()