# Aqui ficará a função de play-pause do programa, todos os pedais 
# vão usar ela.
# 
# Ela ira receber um parametro "nome_tape" pra saber o que estará
# pausando e tocando
# 

# O tk inter não tem um bom reprodutor de sons e por isso estarei usando
# o pygames.mixer pra fazer a nossa reprodução
from pygame import mixer
from pygame import mixer_music

from playsound import playsound

#from pydub import AudioSegment
#from pydub.playback import play

from tkinter import *
#mport tkSnack

'''modelo pygames'''
#mixer.init()
def play(name_tape): 
    print('\n\n tocando')
    mixer.music.load(name_tape)
    mixer.music.play(-1)

'''
#modelo playsound'
def play(name_tape):
    print('\n\n tocando')
    playsound(name_tape)


#modelo pydyb
def play(name_tape):
    song = AudioSegment.from_wav(name_tape)
    play(song)



# modelo tk snack

#testar separadamente

def play(name_tape):
    root = Tk()
    tkSnack.initializeSnack(window)

    snd = tkSnack.Sound()
    snd.read(name_tape)
    snd.play(blocking=1)

#modelo nativo 
import os
def play():

    file = "file.mp3"
    os.system("mpg123 " + file)

#play('pedal_a')
'''