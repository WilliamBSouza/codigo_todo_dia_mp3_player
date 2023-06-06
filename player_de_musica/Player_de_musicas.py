#PASSOS

"""

CRIAR UM MP3 PLAYER QUE EMULE MP3 FÍSICO 
CONSTRUIR UMA INTERFACE PARA O USUÁRIO 
A INTERFACE MOSTRARÁ OS ARQUIVOS MP3 DISPONIVEIS
 

"""

from tkinter import*
from tkinter import filedialog
import pygame
from pygame import mixer
from PIL import Image, ImageTk
import os
import random

#cores
lime = "#00FF00"
alice_blue = "#F0F8FF"
MediumSpringGreen= "#00FA9A"
Branco = '#FFFFFF' 	
preto ='#000000'

def play():

    index_selecionado = listbox.curselection()
    if index_selecionado:
        musica_selecionada = listbox.get(index_selecionado)
        mixer.music.load(musicas_dict[musica_selecionada])
        mixer.music.play()
        rodando = listbox.get(ACTIVE)
        musica_rodando['text'] = rodando  #para que o nome seja alterado esta liha de código deve estar logo em seguida do listbox.get(ACTIVE) caso contrário não troca o nome da musica

def adicionar_musicas():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        for arquivo in os.listdir(pasta_selecionada):
            if arquivo.endswith(".mp3"):
                nome_musica = os.path.splitext(arquivo)[0]
                endereco_musica = os.path.join(pasta_selecionada, arquivo)
                musicas_dict[nome_musica] = endereco_musica
                listbox.insert(END, nome_musica)
   
def pause():
    mixer.music.stop()

def proxima():
    index_selecionado = listbox.curselection()
    if index_selecionado:
        proximo_index = (index_selecionado[0] + 1) % listbox.size()
        listbox.selection_clear(0, END)
        listbox.selection_set(proximo_index)
        listbox.activate(proximo_index)
        listbox.see(proximo_index)
        play()

def anterior():
    index_selecionado = listbox.curselection()
    if index_selecionado:
        anterior_index = (index_selecionado[0] - 1) % listbox.size()
        listbox.selection_clear(0, END)
        listbox.selection_set(anterior_index)
        listbox.activate(anterior_index)
        listbox.see(anterior_index)
        play()   



def mesclar():
    index_selecionado = listbox.curselection()
    if index_selecionado:
        aleatorio_index = random.randint(0, listbox.size() - 1)
        listbox.selection_clear(0, END)
        listbox.selection_set(aleatorio_index)
        listbox.activate(aleatorio_index)
        listbox.see(aleatorio_index)
        play()

janela = Tk()
janela.geometry("800x700")
janela.title('Player mp3')

#variáveis
lista = ['']

# Inicializando variáveis

#frames

#frame esquerda
frame_esquerda = Frame(janela,width=400, height=700,bg=MediumSpringGreen,relief="flat")
frame_esquerda.grid(row=1, column=1,pady=1,padx=0,sticky=NSEW)
img1 = Image.open('icone_central.png')
img1 = img1.resize((250,250))
img1 = ImageTk.PhotoImage(img1)

Ilogo = Label(frame_esquerda,height=250, image=img1,compound=LEFT,padx= 0, anchor='nw', font='ivy 16 bold')#não coloquei bg e fg 
Ilogo.place(x=70,y=150 )

musica_rodando = Label(frame_esquerda, text='Escolha uma musica na lista', width=44, justify=LEFT,anchor='nw',font=('ivy 10'),bg=Branco,fg=preto)
musica_rodando.place(x=25, y=500)

# frame direita 
frame_direita= Frame(janela,width=400, height=700,bg=alice_blue,relief="flat")
frame_direita.grid(row=1, column=2, pady=1, padx=0,sticky=NSEW)


listbox = Listbox(frame_direita,width=40 ,height= 30, selectmode=SINGLE,font=('arial 10 bold'))#também sem bg e fg 
listbox.place(x=60, y=100,)

s= Scrollbar(frame_direita)
s.place(x=340,y=100,height=515)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

for i in lista:
    listbox.insert(END, i)

#imagens para os botões 

img_play = Image.open('play.png')
img_play = img_play.resize((30,30)) # as imagens já estão em 30x30 mas coloquei apenas para garantir a padronização dos botões
img_play = ImageTk.PhotoImage(img_play)

img_pause = Image.open('pause.png')
img_pause = img_pause.resize((30,30)) # as imagens já estão em 30x30 mas coloquei apenas para garantir a padronização dos botões
img_pause = ImageTk.PhotoImage(img_pause)

img_proxima = Image.open('proxima.png')
img_proxima = img_proxima.resize((30,30)) # as imagens já estão em 30x30 mas coloquei apenas para garantir a padronização dos botões
img_proxima = ImageTk.PhotoImage(img_proxima)

img_anterior = Image.open('anterior.png')
img_anterior = img_anterior.resize((30,30)) # as imagens já estão em 30x30 mas coloquei apenas para garantir a padronização dos botões
img_anterior = ImageTk.PhotoImage(img_anterior)

img_aleatório = Image.open('aleatório.png')
img_aleatório = img_aleatório.resize((30,30)) # as imagens já estão em 30x30 mas coloquei apenas para garantir a padronização dos botões
img_aleatório = ImageTk.PhotoImage(img_aleatório)

#botões
botão_play = Button(janela,text="Play",image=img_play,command=play)
botão_play.place(x=173, y=550 )

botão_pause = Button(janela,text="Pause",image=img_pause,command=pause)
botão_pause.place(x=209, y=550 )

botão_proxima = Button(janela,image=img_proxima,text="Próxima", command=proxima)
botão_proxima.place(x=245, y=550 )

botão_anterior = Button(janela,text="Anterior",image=img_anterior, command=anterior)
botão_anterior.place(x=137, y=550 )

botão_aleatório = Button(janela,text="Aleatório",image=img_aleatório, command=mesclar)
botão_aleatório.place(x=101, y=550 )

botão_adicionar_musicas = Button(janela, text="Adicionar Músicas", command=adicionar_musicas)
botão_adicionar_musicas.place(x=550, y=50)



mixer.init()
mixer.init()
musicas_dict = {}  # Dicionário para armazenar o nome da música e o endereço completo

janela.mainloop()