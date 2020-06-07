#bibliotecas
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from pygame import mixer
from webbrowser import open_new


#importação dos arquivos internos
from pedal_a import rec_a
from pedal_s import rec_s
from pedal_d import rec_d
from pedal_f import rec_f


#inicializando o sistema de audio
mixer.init()


'''
=============================
== Configurações da Janela ==
=============================
'''
window = Tk() #inicializando a janela
#tamanho da janela
window.geometry('790x450+260+70')
window.title('Loopyng')

window.iconbitmap(r'../assents/icon.ico') #escolhendo o iconi
#alterando a cor de fundo
window["bg"] = "#BDBDBD"
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
==================
== Fotos Pedais ==
==================
'''

#============ Pedal A =================
def pedal_a_show(): #função que monta o pedal A na  tela
    pedal_a = PhotoImage(file="../assents/Pedal_A.png" ).zoom(2,2)
    area_pedal = Label(window, image=pedal_a, bg='#BDBDBD')#ultimo parametro é o fundo
    area_pedal.pedal_a = pedal_a
    area_pedal.pack()
    area_pedal.place(x= 100, y= 180) #posição do label
    
pedal_a_show() #mostrando o pedal A


def on_a(event): #função que mostra a tecla apertada
    print('teclado')
    pedal_a_out = PhotoImage(file="../assents/Pedal_A_mod.png" ).zoom(2,2)
    area_pedal_out = tk.Label(window, image=pedal_a_out, bg='#BDBDBD')
    area_pedal_out.pedal_a_out = pedal_a_out
    area_pedal_out.pack()
    area_pedal_out.place(x= 100, y= 180)
    
    def out_a(event):
        print('desteclado')
        pedal_a_out.blank() #sumindo com o botão escuro
        pedal_a_show() #mostrando novamente o botão normal 
        
    window.bind('<space>',out_a)
    
window.bind('<a>',on_a)
#==============================

# ====== Pedal S ===============
def pedal_s_show():
    pedal_s = PhotoImage(file="../assents/Pedal_S.png").zoom(2,2)
    area_pedal = Label(window, image=pedal_s, bg='#BDBDBD' )#ultimo parametro é o fundo
    area_pedal.pedal_s = pedal_s
    area_pedal.pack()
    area_pedal.place(x= 250, y= 180)

pedal_s_show() #mostrando o pedal S


def on_s(event): #função que mostra a tecla apertada
    print('teclado')
    pedal_s_out = PhotoImage(file="../assents/Pedal_S_mod.png" ).zoom(2,2)
    area_pedal_out = tk.Label(window, image=pedal_s_out, bg='#BDBDBD')
    area_pedal_out.pedal_s_out = pedal_s_out
    area_pedal_out.pack()
    area_pedal_out.place(x= 250, y= 180)
    
    def out_s(event):
        print('desteclado')
        pedal_s_out.blank() #sumindo com o botão escuro
        pedal_s_show() #mostrando novamente o botão normal 
        
    window.bind('<space>',out_s)
    
window.bind('<s>',on_s)
#==============================

# ===========Pedal D =========
def pedal_d_show():
    pedal_d = PhotoImage(file="../assents/Pedal_D.png").zoom(2,2)
    area_pedal = Label(window, image=pedal_d, bg='#BDBDBD' )#ultimo parametro é o fundo
    area_pedal.pedal_s = pedal_d
    area_pedal.pack()
    area_pedal.place(x= 400, y= 180)

pedal_d_show() #mostrando o pedal d


def on_d(event): #função que mostra a tecla apertada
    print('teclado')
    pedal_d_out = PhotoImage(file="../assents/Pedal_D_mod.png" ).zoom(2,2)
    area_pedal_out = tk.Label(window, image=pedal_d_out, bg='#BDBDBD')
    area_pedal_out.pedal_d_out = pedal_d_out
    area_pedal_out.pack()
    area_pedal_out.place(x= 400, y= 180)
    
    def out_d(event):
        print('desteclado')
        pedal_d_out.blank() #sumindo com o botão escuro
        pedal_d_show() #mostrando novamente o botão normal 
        
    window.bind('<space>',out_d)
    
window.bind('<d>',on_d)
#==========================

# ========== Pedal F =======
def pedal_f_show():
    pedal_f = PhotoImage(file="../assents/Pedal_F.png").zoom(2,2)
    area_pedal = Label(window, image=pedal_f, bg='#BDBDBD' )#ultimo parametro é o fundo
    area_pedal.pedal_f = pedal_f
    area_pedal.pack()
    area_pedal.place(x= 550, y= 180)

pedal_f_show() #mostrando o pedal F


def on_f(event): #função que mostra a tecla apertada
    print('teclado')
    pedal_f_out = PhotoImage(file="../assents/Pedal_F_mod.png" ).zoom(2,2)
    area_pedal_out = tk.Label(window, image=pedal_f_out, bg='#BDBDBD')
    area_pedal_out.pedal_f_out = pedal_f_out
    area_pedal_out.pack()
    area_pedal_out.place(x= 550, y= 180)
    
    def out_f(event):
        print('desteclado')
        pedal_f_out.blank() #sumindo com o botão escuro
        pedal_f_show() #mostrando novamente o botão normal 
        
    window.bind('<space>',out_f)
    
window.bind('<f>',on_f)
#==========================
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
#=====================================

#== Função de fechamento da janela
def on_close():
    print('fechano programa...')
    mixer.quit() #Parano a reprodução do audio
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)#esperando o usuario apertar o botão de fechar
#====================================


'''
==============
== Gravação ==
==============
'''

#chamada dos pedais
pedal_a = rec_a(window)
pedal_s = rec_s(window)
pedal_d = rec_d(window)
pedal_f = rec_f(window)



window.mainloop()




