import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, output_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': output_path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def select_output_path():
    path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, path + '/%(title)s.%(ext)s')

def start_download():
    url = url_entry.get()
    output_path = output_entry.get()
    download_video(url, output_path)

app = tk.Tk()
app.title("Video Downloader")

tk.Label(app, text="Video URL:").pack(padx=10, pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(padx=10, pady=5)

tk.Label(app, text="Output Path:").pack(padx=10, pady=5)
output_entry = tk.Entry(app, width=50)
output_entry.pack(padx=10, pady=5)
tk.Button(app, text="Browse", command=select_output_path).pack(padx=10, pady=5)

tk.Button(app, text="Download", command=start_download).pack(padx=10, pady=20)

app.mainloop()
