#IMPORTS
import yt_dlp 
import tkinter as tk
import customtkinter as ctk

#DOWNLOAD FUNCTION
def download_video():
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            # 'postprocessors': [{
            #     'key': 'FFmpegExtractAudio',
            #     'preferredcodec': 'mp3',
            #     'preferredquality': '192',
            # }],
            # 'cookiesfrombrowser': 'chrome',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([URL.get()])
    except Exception as e:
        print(e)

#SYSTEM SETUP
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#UI SETUP
app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#UI ELEMENTS
title = ctk.CTkLabel(app, text="Insert URL", font=("Roboto", 24))
title.pack(padx=10, pady=10)

URL = tk.StringVar()
link = ctk.CTkEntry(app, placeholder_text="Enter URL", width=350, height=40, textvariable=URL)
link.pack()

#Download Btn
download = ctk.CTkButton(app, text="Download", command=download_video)
download.pack(padx=10, pady=10)



#RUN APP
app.mainloop()