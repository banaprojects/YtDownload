
import tkinter as tk
import customtkinter as ctk
import home

def checkLogin(uname, pwd):
    with open('config.txt', 'r') as f:
        cred = f.read()
        if not cred:
            login(uname, pwd)
        else:
            openNewWindow()


def login(username, password):
    try:
        with open('config.txt', 'w') as f:
            f.write(f'{username}\n{password}')
        openNewWindow()
    except Exception as e:
        print(e)


def openNewWindow():
    app.destroy()
    home.open_window()


#SYSTEM SETUP
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("720x380")
app.title("Youtube Downloader | Signin")

title = ctk.CTkLabel(app, text="Signin", font=("Roboto", 24))
title.pack(padx=10, pady=10)

username = tk.StringVar()
uname = ctk.CTkEntry(app, placeholder_text="Enter YouTube Username", width=250, height=40, textvariable=username)
uname.pack(pady=(40, 10))

password = tk.StringVar()
pwd = ctk.CTkEntry(app, placeholder_text="Enter YouTube Password", width=250, height=40, textvariable=password)
pwd.pack(pady=(40, 20))

log = ctk.CTkButton(app, text="Signin", command=lambda:checkLogin(username.get(), password.get()))
log.pack(padx=10, pady=(15, 10))

app.mainloop()