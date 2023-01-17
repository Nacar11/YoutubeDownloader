# pip install customtkinter
from tkinter import END, messagebox
from pytube import YouTube
import customtkinter
import tkinter.filedialog as fd
import shutil



#read README.md for installation using pyinstaller
customtkinter.set_appearance_mode("light")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.labelPreview1 = customtkinter.CTkLabel(self)
        self.labelPreview2 = customtkinter.CTkLabel(self)
        self.geometry("530x350")
        self.title("Youtube Downloader")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 2), weight=0)
        self.grid_rowconfigure((0, 1, 0), weight=1)
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="YT Downloader", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.preview, text="Preview")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=20)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.download, text="Download")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=20)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.clear, text="Clear")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=20)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Display:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_display)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Place Link here")
        self.entry.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
    def download(self):

     if(self.entry.get()):
      directory = fd.askdirectory()
      print(type(directory))
      print(directory)
      ytLink = self.entry.get()
      yt = YouTube(ytLink)
      vid = yt.streams.get_highest_resolution().download('./YTfolder')
      shutil.move(vid, directory)
     else:
        messagebox.showerror("Error", "Please Enter Link on the Entry Provided Below")

    

    def preview(self): 

     self.labelPreview1.destroy()
     self.labelPreview1 = customtkinter.CTkLabel(self, text="", font=customtkinter.CTkFont(size=12, weight="bold"),  width=120, height=65)
     self.labelPreview1.grid(row=0, column=1, padx=(10, 0), pady=(10, 0))

     ytLink = self.entry.get()
     # label.configure(text=ytLink)
     yt = YouTube(ytLink)
     mytext = "{}  \n\nAuthor: {}  \n\nViews: {}" .format(yt.title, yt.author, yt.views)
     self.labelPreview1 = customtkinter.CTkLabel(self, text=mytext, font=customtkinter.CTkFont(size=12, weight="bold"),  width=120, height=65)
     self.labelPreview1.grid(row=0, column=1, padx=(10, 0), pady=(0, 0))

    def clear(self):

     self.labelPreview1.destroy()
     self.entry.delete(0,END)
        
     self.labelPreview1 = customtkinter.CTkLabel(self, text="", font=customtkinter.CTkFont(size=12, weight="bold"),  width=120, height=65)
     self.labelPreview1.grid(row=0, column=1, padx=(10, 0), pady=(10, 0))

    def change_display(self, new_display: str):

     customtkinter.set_appearance_mode(new_display)

    

if __name__ == "__main__":
    app = App()
    app.mainloop()