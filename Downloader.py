from yt_dlp import YoutubeDL
import os
import customtkinter as customtk

# Simple yt-dlp

# Configuration de la fenetre
customtk.set_appearance_mode("Dark")
customtk.set_default_color_theme("blue")
app = customtk.CTk()
app.geometry("400x300")
app.title("Simple yt-dlp")
app.resizable(False, False)

# Configuration de l'emplacement de telechargement
project_folder = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(os.path.join(project_folder, 'Downloaded')):
    os.mkdir(os.path.join(project_folder, 'Downloaded'))
output_folder = os.path.join(project_folder, 'Downloaded')


# Configuration du telechargement mp3
mp3dl_opts = {
    'format': 'bestaudio[ext=mp3]/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.mp3'),
}

# Configuration du telechargement mp4
mp4dl_opts = {
    'format': 'best[ext=mp4]/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.mp4'),
}


# Configuration de la boite de texte + activation de la boite de texte (pour mettre le lien)
textbox = customtk.CTkTextbox(app, width=355, height=20 , corner_radius=10)
textbox.place(relx=0.5, anchor="center", rely=0.5)


# Message pour dire quoi faire en cas de probleme
URLlabel = customtk.CTkLabel(master=app, text="URL de la vidéo :")
label = customtk.CTkLabel(master=app, text="Si le telechargement ne fonctionne pas, \n verifiez votre connexion internet ainsi que l'URL de la vidéo \n puis redémarrez le logiciel")
URLlabel.place(relx=0.5, anchor="center", y=120)
label.place(relx=0.5, anchor="center", y=40)


# Fonction de telechargement mp4
def DownloadMp4():
    URLS = textbox.get("1.0", "end")
    with YoutubeDL(mp4dl_opts) as ydl:
        ydl.download(URLS)

# Fonction de telechargement mp3
def DownloadMp3():
    URLS = textbox.get("1.0", "end")
    with YoutubeDL(mp3dl_opts) as ydl:
        ydl.download(URLS)


# Mise en place et activation des boutons
buttonmp4 = customtk.CTkButton(app, text="Telecharger en tant que MP4",width=70, height=25, command=DownloadMp4)
buttonmp4.place(relx=0.27, anchor="center", rely=0.63)

buttonmp3 = customtk.CTkButton(app, text="Telecharger en tant que MP3",width=70, height=25, command=DownloadMp3)
buttonmp3.place(relx=0.73, anchor="center", rely=0.63)


# Lancement de l'application
app.mainloop()
