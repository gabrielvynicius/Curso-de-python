import pygame
import tkinter as tk
from tkinter import filedialog, ttk
import json
import os


pygame.mixer.init()


PLAYLIST_FILE = "playlist.json"


playlist = []
paused = False


def carregar_playlist():
    global playlist
    if os.path.exists(PLAYLIST_FILE):
        with open(PLAYLIST_FILE, "r") as file:
            playlist = json.load(file)
        for musica in playlist:
            lista_musicas.insert(tk.END, os.path.basename(musica))  


def salvar_playlist():
    with open(PLAYLIST_FILE, "w") as file:
        json.dump(playlist, file)


def adicionar_musica():
    arquivos = filedialog.askopenfilenames(filetypes=[("Arquivos de áudio", "*.mp3 *.wav")])
    if arquivos:
        for arquivo in arquivos:
            if arquivo not in playlist:
                playlist.append(arquivo)
                lista_musicas.insert(tk.END, os.path.basename(arquivo))  
        salvar_playlist()  


def tocar_musica():
    global paused
    if playlist:
        selecao = lista_musicas.curselection()  
        if selecao:
            index = selecao[0]
            pygame.mixer.music.load(playlist[index])
            pygame.mixer.music.play()
            paused = False 


def pausar_musica():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True


def continuar_musica():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False


def parar_musica():
    pygame.mixer.music.stop()


def remover_musica():
    selecao = lista_musicas.curselection()
    if selecao:
        index = selecao[0]
        playlist.pop(index)
        lista_musicas.delete(index)
        salvar_playlist()  


root = tk.Tk()
root.title("🎵 Player de Música")
root.geometry("400x500")
root.configure(bg="#1e1e1e")


style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 14), background="#1e1e1e", foreground="white")


frame_controles = tk.Frame(root, bg="#1e1e1e")
frame_controles.pack(pady=10)


btn_adicionar = ttk.Button(frame_controles, text="📂 Adicionar", command=adicionar_musica)
btn_adicionar.grid(row=0, column=0, padx=5, pady=5)

btn_remover = ttk.Button(frame_controles, text="🗑️ Remover", command=remover_musica)
btn_remover.grid(row=0, column=1, padx=5, pady=5)


frame_lista = tk.Frame(root)
frame_lista.pack()

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_musicas = tk.Listbox(frame_lista, width=50, height=10, bg="#292929", fg="white", font=("Arial", 12), yscrollcommand=scrollbar.set)
lista_musicas.pack()

scrollbar.config(command=lista_musicas.yview)


frame_controles_musica = tk.Frame(root, bg="#1e1e1e")
frame_controles_musica.pack(pady=10)

btn_tocar = ttk.Button(frame_controles_musica, text="▶️ Tocar", command=tocar_musica)
btn_tocar.grid(row=0, column=0, padx=5, pady=5)

btn_pausar = ttk.Button(frame_controles_musica, text="⏸️ Pausar", command=pausar_musica)
btn_pausar.grid(row=0, column=1, padx=5, pady=5)

btn_continuar = ttk.Button(frame_controles_musica, text="▶️ Continuar", command=continuar_musica)
btn_continuar.grid(row=0, column=2, padx=5, pady=5)

btn_parar = ttk.Button(frame_controles_musica, text="⏹️ Parar", command=parar_musica)
btn_parar.grid(row=0, column=3, padx=5, pady=5)


carregar_playlist()

root.mainloop()
