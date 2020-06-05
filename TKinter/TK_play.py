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

#mixer.init()
def play(name_tape): 
    print('\n\n tocando')
    mixer.music.load(name_tape)
    mixer.music.play(-1)

#play('pedal_a')
