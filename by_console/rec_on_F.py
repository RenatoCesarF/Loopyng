#importação das bibliotecas
from time import sleep
from playsound import playsound
import keyboard

#importando a função de gravação
from record import record


#quando F for clicado chama a função de gravar no "pedal" F
while True:
    #aguardando o pressionamento da letra 'F' 
    keyboard.wait('f')
    
    record('pedal_F.wav')
    #função que realiza a gravação
    # Dentro da função record existe um if para caso a tecla F seja apertada 
    # novamente a gravação sera parada
    # O parametro recebido é o nome do arquivo de audio


    #reproduzindo o audio gravado                                                                                                                                     
    while True:
        playsound('pedal_F.wav')
        if keyboard.is_pressed('f'):
            break