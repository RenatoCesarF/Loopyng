import pyaudio, wave
import os 
import tkinter as tk
from keyboard import is_pressed
from TK_play import play


class rec_f:
    def __init__(self, window, name_tape):
        self.name_tape = name_tape
        self.window = window
        self.key_pressed = False
        window.bind("<f>", self.Key_f)  #bind da tecla F para começar a gravação
        window.bind("<space>", self.Key_space) #bind da tecla ESPAÇO para parar a gravação
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.WAVE_OUTPUT_FILENAME = name_tape

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
        

        #tocando o que foi gravado    
        play(self.name_tape)
 
    #função que ouve a tecla F
    def Key_f(self, event):
        '''
        #apagando o arquivo de audio gravado anteriormente com mesmo nome
        try:
            os.remove('{}'.format(self.name_tape))
        
        except:
            pass
        '''
        self.key_pressed = True
        self.poll()

    #função eu ouve a tecla ESPAÇO
    def Key_space(self, event):
        print('a tecla espaço foi pressionada e esta rodando KeySpace agora')
        self.key_pressed = False
        print('parando gravação')
        self.window.after(1000,self.finishRecording)


    def poll(self):
        if self.key_pressed:
            self.recordFrame()
            
            self.wait = self.window.after(1, self.poll)