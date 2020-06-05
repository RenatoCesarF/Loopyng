#importação das bibliotecas
from time import sleep
from playsound import playsound
import keyboard

#importando a função de gravação
from record import record


#quando D for clicado chama a função de gravar no "pedal" D
while True:
    #aguardando o pressionamento da letra 'D' 
    keyboard.wait('d')

    record('pedal_D.wav')
    #função que realiza a gravação
    # Dentro da função record existe um if para caso a tecla D seja apertada 
    # novamente a gravação sera parada
    # O parametro recebido é o nome do arquivo de audio


    #reproduzindo o audio gravado                                                                                                                                     
    while True:
        playsound('pedal_D.wav')
        if keyboard.is_pressed('d'):
            break