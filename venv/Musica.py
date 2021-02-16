import pygame 
import os
from pygame import mixer
from tkinter import Button, Label, Grid, mainloop, Tk


class Musica:

    def __init__(self, nome, artista, album):
        self.nome = nome
        self.artista = artista
        self.album = album
        self.mixer = mixer.music.load("musicas\glycerine.mp3")
        #self.audioplayer = AudioPlayer("musicas\glycerine.mp3")


    def resumir(self):
        #self.audioplayer.resume()
        self.mixer.music.unpause()

    def reproduzir(self):
        #self.audioplayer.play(block=False)
        self.mixer.music.play()

    def pausar(self):
        print("F")
        #self.audioplayer.pause()
        self.mixer.music.pause()

    def parar(self):
        print("FF")
        self.mixer.music.stop()

    def fechar(self):
        print("FFF")
        #self.mixer.music.close()

    def aumentar_volume(self):
        self.alterar_volume(0.1)

    def diminuir_volume(self):
        self.alterar_volume(-0.1)

    def alterar_volume(self,valor):
        print("FFFF")
        #self.audioplayer.volume()
        self.mixer.music.set_volume(valor)

    def iniciar_interface_grafica(self):
        painel = Tk()

        self.iniciar_labels(painel)
        self.iniciar_botoes(painel)

        painel.mainloop()

    def iniciar_labels(self, painel):
        # Labels Fixas
        label1 = Label(painel, text="Bem Vindo ao Muzic Player!")
        label2 = Label(painel, text="Selecione a música que você deseja ouvir")
        # Labels com os dados do Objeto Musica
        label_nome_musica = Label(painel, text=f"Nome: {self.nome}")
        label_artista_musica = Label(painel, text=f"Artista: {self.artista}")
        label_album_musica = Label(painel, text=f"Album: {self.album}")
        # Label Grids
        label1.grid(row=0, column=1)
        label2.grid(row=1, column=1)
        label_nome_musica.grid(row=2, column=1)
        label_artista_musica.grid(row=3, column=1)
        label_album_musica.grid(row=4, column=1)

    def iniciar_botoes(self,painel):
        # Botões
        bt_reproduzir = Button(painel, text="Reproduzir", command=self.reproduzir())
        bt_resumir = Button(painel, text="Resumir", command=self.resumir())
        bt_pausar = Button(painel, text="Pausar", command=self.pausar)
        bt_parar = Button(painel, text="Parar", command=self.parar)
        bt_volume = Button(painel, text="Volume")
        # Botões Grids
        bt_reproduzir.grid(row=5, column=1)
        bt_resumir.grid(row=6, column=1)
        bt_pausar.grid(row=5, column=2)
        bt_parar.grid(row=5, column=0)
        bt_volume.grid(row=5, column=3)

teste = Musica("Glycerine", "Bush", "MachineHead")
teste.iniciar_interface_grafica()