# #IMPORTS
import yt_dlp 
import tkinter as tk
import customtkinter as ctk
import os


def download_video(credentials, url):
    try:
        username, password = credentials
        # print(username)
        # print(password)
        
        cmd = f"yt-dlp -u {username} -p {password} -f b \"{url}\""
        os.system(cmd)
    except Exception as e:
        print(e)

# url = input("Enter URL: ")
# download_video(url)
def open_window():
    
    credentials = []
    with open('config.txt', 'r') as f:
        for line in f:
            credentials.append(line.strip())

    print(credentials)
    #SYSTEM SETUP
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    #UI SETUP
    app = ctk.CTk()
    app.geometry("720x380")
    app.title("Youtube Downloader")

    #UI ELEMENTS
    title = ctk.CTkLabel(app, text="Insert URL", font=("Roboto", 24))
    title.pack(padx=10, pady=10)

    URL = tk.StringVar()
    link = ctk.CTkEntry(app, placeholder_text="Enter URL", width=350, height=40, textvariable=URL)
    link.pack()

    #Download Btn
    download = ctk.CTkButton(app, text="Download Video", command=lambda:download_video(credentials, URL.get()))
    download.pack(padx=10, pady=10)
    # download = ctk.CTkButton(app, text="Download Audio", command=download_audio(URL.get()))
    # download.pack(padx=10, pady=10)


    # RUN APP
    app.mainloop()