from yt_dlp import YoutubeDL
import os
import customtkinter as customtk

# Simple yt-dlp
# Some code here is not very optimised

# Setting up the window
customtk.set_appearance_mode("Dark")
customtk.set_default_color_theme("blue")
app = customtk.CTk()
app.geometry("400x300")
app.title("Simple yt-dlp")
app.resizable(False, False)

# Setting up the folder where downloaded files go
project_folder = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(os.path.join(project_folder, 'Downloaded')):
    os.mkdir(os.path.join(project_folder, 'Downloaded'))
output_folder = os.path.join(project_folder, 'Downloaded')

# Mp4 and Mp3 Download settings
mp3dl_opts = {
    'format': 'bestaudio[ext=mp3]/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.mp3'),
}

mp4dl_opts = {
    'format': 'best[ext=mp4]/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.mp4'),
}

# Setting up the text box to put the url
textbox = customtk.CTkTextbox(app, width=355, height=20 , corner_radius=10)
textbox.place(relx=0.5, anchor="center", rely=0.5)


# Some Text
URLlabel = customtk.CTkLabel(master=app, text="Video URL :")
label = customtk.CTkLabel(master=app, text="If the download doesn't start or has errors\ncheck your internet connection and the url of the video\nthen restart the software")
URLlabel.place(relx=0.5, anchor="center", y=120)
label.place(relx=0.5, anchor="center", y=40)

# Mp3 and Mp4 download functions

def DownloadMp4():
    URLS = textbox.get("1.0", "end")
    with YoutubeDL(mp4dl_opts) as ydl:
        ydl.download(URLS)

def DownloadMp3():
    URLS = textbox.get("1.0", "end")
    with YoutubeDL(mp3dl_opts) as ydl:
        ydl.download(URLS)


# Setting up and activating buttons
buttonmp4 = customtk.CTkButton(app, text="Download MP4 file",width=70, height=25, command=DownloadMp4)
buttonmp4.place(relx=0.27, anchor="center", rely=0.63)

buttonmp3 = customtk.CTkButton(app, text="Download MP3 file",width=70, height=25, command=DownloadMp3)
buttonmp3.place(relx=0.73, anchor="center", rely=0.63)

# Starting app
app.mainloop()
