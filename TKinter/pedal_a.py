import pyaudio, wave
import os 
import tkinter as tk
from tkinter import *
from keyboard import is_pressed
from TK_play import play
from PIL import Image, ImageTk

#classe gravadora 
class pedal_a:
    def __init__(self, window):
        self.name_tape = 'pedal_a'
        self.window = window
        self.key_pressed = False
        
        pedal_a_show.__init__(self,window)#desenhando o pedal


        #iniciando o sistema de gravação.
        window.bind("<a>", self.Key_a)  #bind da tecla a para começar a gravação
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.WAVE_OUTPUT_FILENAME = self.name_tape

        self.p = pyaudio.PyAudio()
       
        try: self.stream = self.p.open(format=self.FORMAT,
                    channels=self.CHANNELS,
                    rate=self.RATE,
                    input=True,
                    frames_per_buffer=self.CHUNK)
        except:
            return 
        

        self.frames = []

    def recordFrame(self):
        #testes
        #com o frames.append dentro do while e do try
        #Parando gravação
        if is_pressed(' '):
            self.key_pressed = False
        #------------------
        try:
            data = self.stream.read(self.CHUNK)
            print("after try")
            
        except IOError as ex:
            print ("inside except")
            if ex[1] != pyaudio.paInputOverflowed:
                print ("before raise")
                raise
                print( "after raise")

            return None

        self.frames.append(data)

            
    def finishRecording(self):

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        

    #função que ouve a tecla F
    def Key_a(self, event):
        # mostrando o pedal
        pedal_a_out = tk.PhotoImage(file="../assents/Pedal_A_mod.png" ).zoom(2,2)
        self.area_pedal_out = Label(self.window, image= pedal_a_out, bg='#BDBDBD')
        self.area_pedal_out.pedal_a_out = pedal_a_out
        self.area_pedal_out.pack()
        self.area_pedal_out.place(x=100, y=180)

        # acionando o gravador
        self.key_pressed = True
        self.poll()
        

    def poll(self):
        self.window.bind("<space>", self.Key_space) #bind da tecla ESPAÇO para parar a gravação
        if self.key_pressed:
            self.recordFrame()
            
            self.wait = self.window.after(1, self.poll)


    #função eu ouve a tecla ESPAÇO
    def Key_space(self, event):
        #mostrando a tecla
        self.pedal_a = tk.PhotoImage(file="../assents/Pedal_A.png" ).zoom(2,2)
        self.area_pedal = Label(self.window, image= self.pedal_a, bg='#BDBDBD')
        self.area_pedal.pedal_a = self.pedal_a
        self.area_pedal.pack()
        self.area_pedal.place(x=100, y=180)  #posição do label
        #----------

        self.key_pressed = False
        print('parando gravação')
        self.finishRecording()

        #tocando o que foi gravado    
        play(self.name_tape, self.window)


#classe para mostrar e animar a tecla
#
# Partes da classe pedal_a_show foram incorporadas desde já dentro 
#função de gravação pois não estava conseguindo usar dois blind em um mesmo arquivo,
# ou até mesmo em arquivos diferentes. Futuramente consertarei.


class pedal_a_show:
    def __init__(self, window):
        self.window = window

        def on_a():#função que mostra a tecla pressionada
            pedal_a_out = tk.PhotoImage(file="../assents/Pedal_A_mod.png" ).zoom(2,2)
            self.area_pedal_out = Label(window, image= pedal_a_out, bg='#BDBDBD')
            self.area_pedal_out.pedal_a_out = pedal_a_out
            self.area_pedal_out.pack()
            self.area_pedal_out.place(x=100, y=180)
            
        def show_a(self):#função que mostra a tecla normal, não pressionada
            self.pedal_a = tk.PhotoImage(file="../assents/Pedal_A.png" ).zoom(2,2)
            self.area_pedal = Label(window, image= self.pedal_a, bg='#BDBDBD')
            self.area_pedal.pedal_a = self.pedal_a
            self.area_pedal.pack()
            self.area_pedal.place(x=100, y=180)  #posição do label

            def out_a(event): #função que chama a função de mostrar tecla pressionada e apaga a tecla normal
                on_a()
                self.pedal_a.blank()

                #linha que espera o comando espaço para resetar o sistema de animação
                window.bind('<space>',show_a)

            window.bind('<o>', out_a)#esperando a tecla A para pressonar a letra


        show_a(window)  # esta linah apenas chama a função ao iniciar
        
        def teste():
            print('flsdjfsldkfjjksd\b\b\b')