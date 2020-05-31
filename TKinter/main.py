#bibliotecas
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer_music
from pygame import mixer
import webbrowser

#importação dos arquivos internos
from TK_record import Pedal_rec
from TK_play import play
#from key_pressed import key_pressed


#inicializando o player
mixer.init()

'''
=============================
== Configurações da Janela ==
=============================
'''
window = Tk()
window.title('Loopyng')
#tamanho da janela
window.geometry('800x450+260+70')
#alterando o fundo da imagem
window["bg"] = "#BDBDBD"
#definição do tamanho ta janela
window.maxsize(800,450)


'''
========================================
== Configuração dos elementos da tela ==
========================================
'''
# logo do cabeçalho
logo = PhotoImage(file="../assents/logo.png").subsample(2, 2) 
area_logo = Label(window, image=logo, bg='#BDBDBD' )#ultimo parametro é o fundo
area_logo.logo = logo
area_logo.pack()


#texto do cabeçalho
text_header = Label(window, text='Aperte uma das teclas para começar a gravar, e depois ESPAÇO para parar', bg='#BDBDBD',font=("HarvestItal", 15),fg='#2D2D2D')
text_header.place(x= 60, y = 130)


'''
================
== Foto Pedais==
================
'''
# Pedal A
pedal_a = PhotoImage(file="../assents/Pedal_A.png").zoom(2,2)
area_pedal = Label(window, image=pedal_a, bg='#BDBDBD' )#ultimo parametro é o fundo
area_pedal.pedal_a = pedal_a
area_pedal.pack()
area_pedal.place(x= 100, y= 180)

# Pedal S
pedal_s = PhotoImage(file="../assents/Pedal_S.png").zoom(2,2)
area_pedal = Label(window, image=pedal_s, bg='#BDBDBD' )#ultimo parametro é o fundo
area_pedal.pedal_s = pedal_s
area_pedal.pack()
area_pedal.place(x= 250, y= 180)

# Pedal D
pedal_d = PhotoImage(file="../assents/Pedal_D.png").zoom(2,2)
area_pedal = Label(window, image=pedal_d, bg='#BDBDBD' )#ultimo parametro é o fundo
area_pedal.pedal_s = pedal_d
area_pedal.pack()
area_pedal.place(x= 400, y= 180)

# Pedal F
pedal_f = PhotoImage(file="../assents/Pedal_F.png").zoom(2,2)
area_pedal = Label(window, image=pedal_f, bg='#BDBDBD' )#ultimo parametro é o fundo
area_pedal.pedal_f = pedal_f
area_pedal.pack()
area_pedal.place(x= 550, y= 180)
'''
================
== GitHub Link==
================
'''
#Icon github
github = PhotoImage(file="../assents/github_icon.png").subsample(4, 4) 
github_icon = Label(window, image = github, bg='#BDBDBD')#ultimo parametro é o fundo
github_icon.github_icon = github
github_icon.pack()
github_icon.place(x= 0, y = 400)

def callback(event):
    webbrowser.open_new(event.widget.cget('text'))
#Link/text
link_git = Label(window,text=r"https://github.com/RenatoCesarF/Loopyng",font=("arial", 10), fg="#939694", cursor="hand2", bg='black')
link_git.pack()
link_git.place(x= 47, y = 415)

link_git.bind("<Button-1>", callback)
#=====================================


#------------
#--GRAVAÇÃO--
#------------

#passar a função inteira de keylistner aqui para dentro
# refazer o sistema de gravação

window.mainloop()




