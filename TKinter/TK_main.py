from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from pygame import mixer
from webbrowser import open_new


#importação dos arquivos internos
from pedal_a import pedal_a
from pedal_s import pedal_s
from pedal_d import pedal_d
from pedal_f import pedal_f



mixer.init() #inicializando o sistema de audio


'''
=============================
== Configurações da Janela ==
=============================
'''
window = Tk() #inicializando a janela
window.geometry('790x450+260+70')#tamanho da janela
window.title('Loopyng')
window.iconbitmap(r'../assents/icon.ico') #escolhendo o iconi
window["bg"] = "#BDBDBD" #alterando a cor de fundo

#definição do tamanho ta janela
window.maxsize(790, 450)
window.minsize(690, 300)



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
text_header.place(x= 70, y = 130)


'''
============
== Pedais ==
============
'''

#========== Pedal A =========|
pedal_a(window)

#========== Pedal S =========|
pedal_s(window)

#========== Pedal D =========|
pedal_d(window)

#========== Pedal F =========|
pedal_f(window)

'''
===========================
== outras funcionalidades==
===========================
'''
#=== Redirecionando usuário para o github do projeto ===#

#Icon github
github = PhotoImage(file="../assents/github_icon.png").subsample(4, 4) 
github_icon = Label(window, image = github, bg='#BDBDBD', cursor="hand2")#ultimo parametro é o fundo
github_icon.github_icon = github
github_icon.pack(side=BOTTOM, anchor=SW)


def git_redirect(event): #função que redireciona para a pagina no github
    webbrowser.open_new('https://github.com/RenatoCesarF/Loopyng')
    
github_icon.bind("<Button-1>", git_redirect)# Detectar se o botão esquerdo do mause foi clicado no ícone, caso sim, ele chama o redirecionamento


#== Função de fechamento da janela
def on_close():
    print('fechano programa...')
    mixer.quit() #Parano a reprodução do audio
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)#esperando o usuario apertar o botão de fechar
#====================================


window.mainloop()




