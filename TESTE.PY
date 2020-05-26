#importação das bibliotecas
from time import sleep
from playsound import playsound
import keyboard

#importando a função de gravação


#quando A for clicado chama a função de gravar no "pedal" A 


#reproduzindo o audio gravado                                                                                                                                     
while True:
    playsound('pedal_S.wav')
    if keyboard.is_pressed('a'):
        break