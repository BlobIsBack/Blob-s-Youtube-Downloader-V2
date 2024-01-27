from yt_dlp import YoutubeDL
import os
import customtkinter as customtk

# Configuration de la fenetre
customtk.set_appearance_mode("Dark")
customtk.set_default_color_theme("blue")
app = customtk.CTk()
app.geometry("400x300")
app.title("Blob's Youtube Downloader")
app.resizable(False, False)

# Configuration de l'emplacement de telechargement
project_folder = os.path.dirname(os.path.realpath(__file__))
output_folder = os.path.join(project_folder, 'Downloaded')

ydl_ops = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.mp3'),
}

dl_ops = {
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s')
}

textbox = customtk.CTkTextbox(app, width=355, height=20 , corner_radius=10)
textbox.place(relx=0.5, anchor="center", rely=0.5)

URLlabel = customtk.CTkLabel(master=app, text="URL de la vidéo :")
label = customtk.CTkLabel(master=app, text="Si le telechargement ne fonctionne pas, \n verifiez votre connexion internet ainsi que l'URL de la vidéo \n puis redémarrez le logiciel")
URLlabel.place(relx=0.5, anchor="center", y=120)
label.place(relx=0.5, anchor="center", y=40)

def DownloadMp4():
    URLS = textbox.get("1.0", "end")
    with YoutubeDL(dl_ops) as ydl:
        ydl.download(URLS)

def DownloadMp3():
    URLS = textbox.get("1.0", "end")
    with YoutubeDL(ydl_ops) as ydl:
        ydl.download(URLS)

buttonmp4 = customtk.CTkButton(app, text="Telecharger en tant que MP4",width=70, height=25, command=DownloadMp4)
buttonmp4.place(relx=0.27, anchor="center", rely=0.63)

buttonmp3 = customtk.CTkButton(app, text="Telecharger en tant que MP3",width=70, height=25, command=DownloadMp3)
buttonmp3.place(relx=0.73, anchor="center", rely=0.63)

app.mainloop()