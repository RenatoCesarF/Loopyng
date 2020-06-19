5# Aqui ficará a função de play-pause do programa, todos os pedais 
# vão usar ela.
# 
# Ela ira receber um parametro "nome_tape" pra saber o que estará
# pausando e tocando
# 

# O tk inter não tem um bom reprodutor de sons e por isso estarei usando
# o pygames.mixer pra fazer a nossa reprodução

from pygame import mixer
from pygame import mixer_music
from pygame import time
from tkinter import *

mixer.init()

def play(name_tape,window):
    
    pause = False
    
    print('\n\n tocando')
    mixer.music.load(name_tape) #carregando o arquivo de audio
    som = mixer.Sound(name_tape)#transformando-o em um objeto
    largura = mixer.Sound.get_length(som)#definindo o tamanho do 
    
    my_delay = int((largura * 1000) - 400)  # transformando a largura em delay, multiplica-se por 1000 para conseguir
                                            # o tempo em segundos, e depois tira-se outro valor para eliminar o 1 segundo
                                            # de delay que existe no pygames.

    
    #reproduzindo infinitamente o audio, com um delay definido acima.
    def init_loop():

        mixer.Sound.play(som)
        window.after(my_delay, init_loop)
        
    init_loop()
    
