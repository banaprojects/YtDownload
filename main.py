#IMPORTS
import yt_dlp 
import tkinter as tk
import customtkinter as ctk
import os

#DOWNLOAD FUNCTION
def download_video():
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([URL.get()])
    except Exception as e:
        print(e)

def download_audio():
    try:
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': '%(title)s.%(ext)s',
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
app.geometry("720x280")
app.title("Youtube Downloader")

#UI ELEMENTS
title = ctk.CTkLabel(app, text="Insert URL", font=("Roboto", 24))
title.pack(padx=10, pady=10)

URL = tk.StringVar()
link = ctk.CTkEntry(app, placeholder_text="Enter URL", width=350, height=40, textvariable=URL)
link.pack()

#Download Btn
download = ctk.CTkButton(app, text="Download Video", command=download_video)
download.pack(padx=10, pady=10)
download = ctk.CTkButton(app, text="Downoad Audio", command=download_audio)
download.pack(padx=10, pady=10)


#RUN APP
app.mainloop()