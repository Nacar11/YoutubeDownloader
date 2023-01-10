# pip install customtkinter
from pytube import YouTube
from PIL import Image, ImageTk
from urllib.request import urlopen
import customtkinter
import tkinter
import tkinter.messagebox
# import ytDownloader
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.labelPreview1 = customtkinter.CTkLabel(self)
        self.labelPreview2 = customtkinter.CTkLabel(self)
        self.geometry("850x550")
        self.title("Youtube Downloader")

         # configure grid layout (4x4)
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
        # ytLink= StringVar()
        # yt = YouTube(ytLink)

        # self.previewTitle = customtkinter.CTkLabel(master=self, text="", text_color="black",  width=120, height=35,)

        # self.previewTitle.pack(pady=5, padx=12)

        # self.previewView = customtkinter.CTkLabel(master=self, text=("Views:", ""), text_color="black",  width=120, height=35,)

        # self.previewView.pack(pady=10, padx=12)
 

    def download():
        print("test")
    #  ytLink = entry1.get()
    #  # label.configure(text=ytLink)
    #  yt = YouTube(ytLink)

    #  yd = yt.streams.get_highest_resolution()

    #  # ADD FOLDER HERE
    #  yd.download('./YTfolder')
    

    def preview(self): 
     
     
     self.clear()
    

     ytLink = self.entry.get()
     # label.configure(text=ytLink)
     
     yt = YouTube(ytLink)
     self.labelPreview1 = customtkinter.CTkLabel(self, text=yt.title, font=customtkinter.CTkFont(size=12, weight="bold"), text_color="black",  width=120, height=65)
     self.labelPreview1.grid(row=0, column=1, padx=(10, 0), pady=(10, 0))

     image_url = yt.thumbnail_url
     u = urlopen(image_url)
     raw_data = u.read()
     u.close()
     
     image_final = ImageTk.PhotoImage(data=raw_data)
     
     
     self.labelPreview2 = customtkinter.CTkLabel(self,image=image_final)
     self.labelPreview2.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))

     

    def clear(self):
        self.labelPreview1.destroy()
        self.labelPreview2.destroy()
        self.labelPreview1 = customtkinter.CTkLabel(self, text="", font=customtkinter.CTkFont(size=12, weight="bold"), text_color="black",  width=120, height=65)
        self.labelPreview1.grid(row=0, column=1, padx=(10, 0), pady=(10, 0))
        self.labelPreview2 = customtkinter.CTkLabel(self)

    def change_display(self, new_display: str):
         customtkinter.set_appearance_mode(new_display)

    

     
     


# frame1 = customtkinter.CTkFrame(master=root)
# frame1.pack(side="top", fill="both", expand=True)

# label = customtkinter.CTkLabel(master=frame1, text="Youtube Downloader", text_color="blue",  width=120, height=35,)
# label.pack(pady=20, padx=12)


# entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Place Link Here", textvariable = ytLink, width=400, height=40, border_width=3, font=("Heveltica", 12))
# entry1.pack(pady=15, padx=12)




# button1 = customtkinter.CTkButton(frame1, text="Preview", command=preview)
# button1.pack(pady=12, padx=12)

# button2 = customtkinter.CTkButton(frame1, text="Download", command=download)
# button2.pack(pady=12, padx=12)


if __name__ == "__main__":
    app = App()
    app.mainloop()