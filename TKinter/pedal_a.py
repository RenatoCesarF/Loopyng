from pygame import mixer
from pygame import mixer_music
from tkinter import *

mixer.init()
window = Tk()


mixer.music.load('loop_s.wav')

def key_pressed(Key):
    if Key.char == 'a':
        print('rodando')
        mixer.music.play(1)
    



window.bind("<Key>", key_pressed)


window.mainloop()
