#esse código sera responsável por ouvir o teclado para que o mesmo
#funcione como controle da gravação e reprodução dos audios atraves
# da chamada das outras funções/arquivos.

#importação das bibliotecas usadas
import keyboard
from playsound import playsound
from pynput.keyboard import Key, Listener
from time import sleep

#importação da função de gravação
from recording import record


#quando F for clicado chama a função de gravar no "pedal" F
def rec_on_F():
    
    #aguardando o pressionamento da letra 'F' 
    keyboard.wait('f')
    print('começando a gravar em...')
    sleep(1)
    print('\n 3...')
    sleep(1)
    print('\n 2...')
    sleep(1)
    print('\n 1...')

    record('pedal_F.wav')
    #função que realiza a gravação
    # Dentro da função record existe um if para caso a tecla F seja apertada 
    # novamente a gravação sera parada
    # O parametro recebido é o nome do arquivo de audio 

    #reproduzindo o audio gravado
    while True:
        playsound('pedal_F.wav')

        #esperando que a pessoa reaperte a tecla F para assim parar a reprodução
        if keyboard.is_pressed("f"):
            print('Reprodução parada')
            break
rec_on_F()