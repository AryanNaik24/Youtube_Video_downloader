import tkinter
import customtkinter
from pytube import YouTube

#function to download link
def startDownload():
    try:
        
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text = ytObject.title, text_color = "white")
        finishLabel.configure(text = "")
        video.download()
        finishLabel.configure(text = "Download Complete!",text_color="white")
    except:
        finishLabel.configure(text = "Download Error!",text_color="red")
    
#progress percentage
def on_progress(stream,chunk,bytesRemaining):
    totalSize = stream.filesize
    bytesDownloaded = totalSize - bytesRemaining
    percentageCompletion = bytesDownloaded / totalSize * 100
    per = str(int(percentageCompletion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()
    
    #update progressbar
    pBar.set(float(percentageCompletion)/100)
    
#system settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

#app frame (size type etc)
app = customtkinter.CTk()
#resolution/screen size
app.geometry("720x480")
#app title
app.title("Youtube Downloader")

#adding UI
title = customtkinter.CTkLabel( app , text = "Insert Youtube link ")
title.pack(padx=10,pady=10)

#link insert
urlVar = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350,height=50,textvariable=urlVar)
link.pack()

#finished downloading
finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack()

#progress percentage
pPercentage = customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

#progress bar
pBar = customtkinter.CTkProgressBar(app,width=350)
pBar.set(0)
pBar.pack()

#Download button
download = customtkinter.CTkButton(app,text="Download",width=100,height=60,command=startDownload)
download.pack(padx=10,pady=10)

#runs the app
app.mainloop()