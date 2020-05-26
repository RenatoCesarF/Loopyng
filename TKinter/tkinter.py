import os
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import webbrowser
#importação dos pedais
from TK_record import AppRecording






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
window["bg"] = "#3E3D41"
#definição do tamanho ta janela
window.maxsize(800,450)


'''
========================================
== Configuração dos elementos da tela ==
========================================
'''
#colocando a logo no programa
logo = PhotoImage(file="../assents/logo.png").subsample(2, 2) 
area_logo = Label(window, image=logo, bg='#3E3D41' )#ultimo parametro é o fundo
area_logo.logo = logo
area_logo.pack()


#texto do cabeçalho
text_header = Label(window, text='Aperte uma das teclas para começar a gravar, e depois "espaço" para parar', bg='#3E3D41',font=("HarvestItal", 15),fg='#939694')
text_header.place(x= 60, y = 130)

#====================================
#-- GitHub Link--
#----------------
#imagem do github
github = PhotoImage(file="../assents/github_icon.png").subsample(4, 4) 
github_icon = Label(window, image = github, bg='#3E3D41')#ultimo parametro é o fundo
github_icon.github_icon = github
github_icon.pack()
github_icon.place(x= 0, y = 400)

def callback(event):
    webbrowser.open_new(event.widget.cget('text'))
#Link/texto
link_git = tk.Label(window,text=r"https://github.com/RenatoCesarF/Loopyng",font=("arial", 10), fg="#939694", cursor="hand2", bg='black')
link_git.pack()
link_git.place(x= 47, y = 415)

link_git.bind("<Button-1>", callback)
#=====================================

#---------------
#--botão teste--
#---------------


pedal_A = AppRecording(window) #linha que chama a class de gravação
pedal_S = AppRecording(window)


#===============

window.mainloop()




