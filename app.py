import tkinter as tk
import customtkinter as ct
from pytube import YouTube

def start_download():
    try:
        yt_link = link.get()
        yt_obj = YouTube(yt_link,on_progress_callback=on_progress)
        yt_vid = yt_obj.streams.get_highest_resolution()

        title.configure(text = yt_obj.title,text_color = "white")
        fin.configure(text = "")
        if yt_vid is not None:
            yt_vid.download()
        fin.configure(text = "Downloaded!")
    except:
        fin.configure(text = "YouTube link is Invalid!",text_color = "red")

def on_progress(stream,chunk,bytes_rem):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_rem
    percentage = bytes_downloaded / total_size * 100
    pr = str(int(percentage))
    pro_per.configure(text = pr + "%")
    pro_per.update()

    #update the progress bar
    pro_bar.set(float(pr) / 100)



#Setting Defaults
ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

#App dimensions and settings
app = ct.CTk()
app.geometry("480x300")
app.title("YouTube Video Downloader")


#Add UI
title = ct.CTkLabel(app,text = "Insert A YouTube URL")#we pass the "app" object into the CTkLabel to show where the label should be inside the app frame
title.pack(padx = 5, pady = 5)

#Adding Link
url_var = tk.StringVar()
link = ct.CTkEntry(app,width = 300, height = 30,textvariable=url_var)
link.pack()

#Finished Downloading
fin = ct.CTkLabel(app,text="")
fin.pack()

#Download button
down = ct.CTkButton(app,text="Download",command=start_download)
down.pack(padx = 5,pady = 5)

#Progress number / Percentage
pro_per = ct.CTkLabel(app,text="0%")
pro_per.pack()

pro_bar = ct.CTkProgressBar(app,width = 300)
pro_bar.set(0)
pro_bar.pack(padx = 5, pady = 5)

#Run app
app.mainloop()