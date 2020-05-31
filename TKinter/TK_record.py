import pyaudio, wave 
import tkinter as tk
#Classe de um programa de gravação, não sei nada sobre classes, depois de estudar
#adaptarei essa classe ao meu programa

class Pedal_rec:
    def __init__(self, window,name_tape):
        self.window = window
        self.mouse_pressed = False
        recordingButton = tk.Button(window, text = "")
        recordingButton.pack()
        recordingButton.bind("<ButtonPress-1>", self.OnMouseDown)
        recordingButton.bind("<ButtonRelease-1>", self.OnMouseUp)
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
        try:
            data = self.stream.read(self.CHUNK)
            print ("after try")
        except IOError as ex:
            print ("inside except")
            if ex[1] != pyaudio.paInputOverflowed:
                print ("before raise")
                raise
                print( "after raise")

            data = '\x00' * self.CHUNK  # or however you choose to handle it, e.g. return None

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
 
    #mudar "onMouseDown" por "OnKeyDown"
    def OnMouseDown(self, event):
        self.mouse_pressed = True
        self.poll()

    def OnMouseUp(self, event):
        self.window.after_cancel(self.after_id)
        print ("Finished recording!")
        self.finishRecording()
        

    def poll(self):
        if self.mouse_pressed:
            self.recordFrame()
            self.after_id = self.window.after(1, self.poll)
