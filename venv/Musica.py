from tkinter import Button, Label, Grid, mainloop, Tk
from pygame import mixer
import os
import random

class playlist():

    def __init__(self):
        self.lista_musicas = self.montar_lista_musicas("musicas")
        self.mixer = mixer
        self.musica_atual = 0
        # self.lista_nomes = self.nome_musicas("musicas")
        # self.nome_musica_atual = self.lista_nomes[self.musica_atual]

    def montar_lista_musicas(self, caminho):
        playlist = []
        diretorio = os.listdir(caminho)
        for musicas in diretorio:
            playlist.append(os.path.join(caminho, musicas))
        return playlist

    def resumir(self):
        self.mixer.music.unpause()

    def reproduzir(self):
        self.mixer.init()
        self.mixer.music.load(self.lista_musicas[self.musica_atual])
      #  print(f"Musica atual no reproduzir: {self.nome_musica_atual}")
        self.mixer.music.play()

    def pausar(self):
        self.mixer.music.pause()

    def parar(self):
        self.mixer.music.stop()

    def fechar(self):
        self.mixer.quit()

    def proxima_musica(self):
        if((self.musica_atual + 1) > (len(self.lista_musicas) - 1) ):
            print("Última música da playlist")
        else:
            self.musica_atual += 1
            self.parar()
            self.reproduzir()

    def musica_anterior(self):
        if ((self.musica_atual - 1) < 0  ):
            print("Primeira música da playlist")
        else:
            self.musica_atual -= 1
            self.parar()
            self.reproduzir()

    def aumentar_volume(self):
        self.__alterar_volume(0.1)

    def diminuir_volume(self):
        self.__alterar_volume(-0.1)

    def __alterar_volume(self, valor):
        if (self.mixer.music.get_volume() + valor < 0):
            self.mixer.music.set_volume(0)
        else:
            self.mixer.music.set_volume(self.mixer.music.get_volume() + valor)

    def nome_musicas(self,caminho):
        diretorio = os.listdir(caminho)
        nomes = []
        for musicas in diretorio:
            nomes.append(musicas)
        return nomes

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
        label_nome_musica = Label(painel, text="Nome: Ilustrativo")
        label_artista_musica = Label(painel, text="Artista: Inventado")
        label_album_musica = Label(painel, text=f"Album: Iluminismo")
        # Label Grids
        label1.grid(row=0, column=1)
        label2.grid(row=1, column=1)
        label_nome_musica.grid(row=2, column=1)
        label_artista_musica.grid(row=3, column=1)
        label_album_musica.grid(row=4, column=1)

    def iniciar_botoes(self, painel):
        # Botões
        bt_reproduzir = Button(painel, text="Reproduzir", command=self.reproduzir)
        bt_resumir = Button(painel, text="Resumir", command=self.resumir)
        bt_pausar = Button(painel, text="Pausar", command=self.pausar)
        bt_parar = Button(painel, text="Parar", command=self.parar)
        bt_proxima = Button(painel, text=">", command=self.proxima_musica)
        bt_anterior = Button(painel, text="<", command=self.musica_anterior)
        bt_aumentar_volume = Button(painel, text="+", command=self.aumentar_volume)
        bt_diminuir_volume = Button(painel, text="-", command=self.diminuir_volume)
        # Botões Grids
        bt_reproduzir.grid(row=5, column=1)
        bt_proxima.grid(row=6, column=2)
        bt_anterior.grid(row=6, column=0)
        bt_pausar.grid(row=5, column=2)
        bt_parar.grid(row=5, column=0)
        bt_aumentar_volume.grid(row=5, column=3)
        bt_diminuir_volume.grid(row=5, column=4)
        bt_resumir.grid(row=6, column=1)

class Musica:

    def __init__(self, nome, artista, album):
        self.nome = nome
        self.artista = artista
        self.album = album
        self.mixer = mixer
        #self.musica_atual


teste_aplicativo = playlist()
teste_aplicativo.iniciar_interface_grafica()

#teste_aplicativo.nome_musicas("musicas")
