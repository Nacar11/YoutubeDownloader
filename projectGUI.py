# pip install customtkinter
from pytube import YouTube
from tkinter import WORD, StringVar, Text
import customtkinter
# import ytDownloader
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root  = customtkinter.CTk()
root.geometry("500x700")
root.title("YoutubeDownloaderNacar")

ytLink= StringVar()

def download():
    
     ytLink = entry1.get()
     # label.configure(text=ytLink)
     yt = YouTube(ytLink)

    

     yd = yt.streams.get_highest_resolution()

     # ADD FOLDER HERE
     yd.download('./YTfolder')
    
def preview():
    
     ytLink = entry1.get()
     # label.configure(text=ytLink)
     yt = YouTube(ytLink)

     print("Title: ", yt.title)

     print("View: ", yt.views)

     previewTitle = customtkinter.CTkLabel(master=frame1, text=yt.title, text_color="black",  width=120, height=35,)

     previewTitle.pack(pady=5, padx=12)

     previewView = customtkinter.CTkLabel(master=frame1, text=("Views:", yt.views), text_color="black",  width=120, height=35,)

     previewView.pack(pady=10, padx=12)

     
     


frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(side="top", fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame1, text="Youtube Downloader", text_color="blue",  width=120, height=35,)
label.pack(pady=20, padx=12)


entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Place Link Here", textvariable = ytLink, width=400, height=40, border_width=3, font=("Heveltica", 12))
entry1.pack(pady=15, padx=12)




button1 = customtkinter.CTkButton(frame1, text="Preview", command=preview)
button1.pack(pady=12, padx=12)

button2 = customtkinter.CTkButton(frame1, text="Download", command=download)
button2.pack(pady=12, padx=12)



root.mainloop()