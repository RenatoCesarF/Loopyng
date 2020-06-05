#importação das bibliotecas
from time import sleep
from playsound import playsound
import keyboard

#importando a função de gravação
from record import record


#quando S for clicado chama a função de gravar no "pedal" S
while True:
    #aguardando o pressionamento da letra 'S' 
    keyboard.wait('s')
    
    #função que realiza a gravação
    record('pedal_S.wav')
    # Dentro da função record existe um if para caso a tecla A seja apertada 
    # novamente a gravação sera parada
    # O parametro recebido é o nome do arquivo de audio


    #reproduzindo o audio gravado                                                                                                                                     
    while True:
        playsound('pedal_S.wav')
        if keyboard.is_pressed('s'):
            break