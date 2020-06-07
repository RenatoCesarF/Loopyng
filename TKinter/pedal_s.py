import pyaudio, wave
import os 
import tkinter as tk
from keyboard import is_pressed
from TK_play import play


class rec_s:
    def __init__(self, window):
        self.name_tape = 'pedal_s'
        self.window = window
        self.key_pressed = False
        window.bind("<s>", self.Key_s)  #bind da tecla s para começar a gravação
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
            return None

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
    def Key_s(self, event):
        
        self.key_pressed = True
        self.poll()

    def poll(self):
        self.window.bind("<space>", self.Key_space) #bind da tecla ESPAÇO para parar a gravação
        if self.key_pressed:
            self.recordFrame()
            
            self.wait = self.window.after(1, self.poll)


    #função eu ouve a tecla ESPAÇO
    def Key_space(self, event):
        print('a tecla espaço foi pressionada e esta rodando KeySpace agora')
        self.key_pressed = False
        print('parando gravação')
        self.finishRecording()

        #tocando o que foi gravado    
        def play_tk():
            play(self.name_tape)
        self.window.after(1000, play_tk)

