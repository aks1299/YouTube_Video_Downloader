import os
import tkinter as tk
from tkinter import filedialog
import customtkinter as ct
import yt_dlp
import re

def validate_url(url):
    youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+')
    return youtube_regex.match(url)

def choose_directory():
    directory = filedialog.askdirectory(initialdir=path_var.get())
    if directory:
        path_var.set(directory)

def start_download():
    yt_link = link.get()
    download_path = path_var.get()
    if not validate_url(yt_link):
        fin.configure(text="Invalid YouTube URL!", text_color="red")
        return

    ydl_opts = {
        'format': f'best[height<={quality_var.get().replace("p", "")}]',
        'progress_hooks': [on_progress],
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s')
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(yt_link, download=True)
            if result is None:
                raise Exception("Failed to extract video information.")
            title.configure(text=result['title'], text_color="white")
            fin.configure(text="Downloaded!", text_color="green")
    except Exception as e:
        fin.configure(text="Error: " + str(e), text_color="red")

def on_progress(d):
    if d['status'] == 'downloading':
        total_size = d.get('total_bytes', 1)
        bytes_downloaded = d.get('downloaded_bytes', 0)
        percentage = bytes_downloaded / total_size * 100
        pr = str(int(percentage))
        pro_per.configure(text=pr + "%")
        pro_per.update()
        pro_bar.set(float(pr) / 100)
    elif d['status'] == 'finished':
        pro_per.configure(text="100%")
        pro_bar.set(1)

# Setting Defaults
ct.set_appearance_mode("System")
ct.set_default_color_theme("dark-blue")

# Set default download path to Downloads folder in C drive
default_path = os.path.join(os.path.expanduser("~"), "Downloads")

# App dimensions and settings
app = ct.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

# Add UI
title = ct.CTkLabel(app, text="Insert A YouTube URL")
title.pack(padx=5, pady=5)

# Adding Link
url_var = tk.StringVar()
link = ct.CTkEntry(app, width=300, height=30, textvariable=url_var)
link.pack(padx=5, pady=5)

# Quality Selection
quality_var = tk.StringVar(value="Select Quality")
quality_options = ["360p", "480p", "720p", "1080p"]
quality_menu = ct.CTkOptionMenu(app, values=quality_options, variable=quality_var)
quality_menu.pack(padx=5, pady=5)

# Choose Download Path
path_var = tk.StringVar(value=default_path)
choose_path_button = ct.CTkButton(app, text="Choose Download Directory", command=choose_directory)
choose_path_button.pack(padx=5, pady=5)
path_entry = ct.CTkEntry(app, width=300, height=30, textvariable=path_var, state='readonly')
path_entry.pack(padx=5, pady=5)

# Finished Downloading
fin = ct.CTkLabel(app, text="")
fin.pack(padx=5, pady=5)

# Download button
down = ct.CTkButton(app, text="Download", command=start_download)
down.pack(padx=5, pady=5)

# Progress number / Percentage
pro_per = ct.CTkLabel(app, text="0%")
pro_per.pack(padx=5, pady=5)

pro_bar = ct.CTkProgressBar(app, width=300)
pro_bar.set(0)
pro_bar.pack(padx=5, pady=5)

# Run app
app.mainloop()
