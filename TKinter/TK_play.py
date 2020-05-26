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
from keyboard import is_pressed
from time import sleep

def loop(name_tape, letter):
    mixer.music.load('{}'.format(name_tape))
    mixer.music.play(-1)
    while True:
        mixer.music.play(-1)  #o -1 é apenas para que o audio seja tocato eternamente
        if is_pressed(letter):
            mixer_music.stop()
            sleep()
        if is_pressed(letter):
            mixer.music.play(-1)


    #adicionar keylistner para pause e play e reset(deletar gravação e possibilitar regravação)
