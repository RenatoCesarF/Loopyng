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


#quando A for clicado chama a função de gravar no "pedal" A
def rec_on_A():

    #aguardando o pressionamento da letra 'A' 
    keyboard.wait('a')
    print('começando a gravar em...')
    sleep(1)
    print('\n 3...')
    sleep(1)
    print('\n 2...')
    sleep(1)
    print('\n 1...')

    record('pedal_A.wav')
    #função que realiza a gravação
    # Dentro da função record existe um if para caso a tecla A seja apertada 
    # novamente a gravação sera parada
    # O parametro recebido é o nome do arquivo de audio
    
    #reproduzindo o audio gravado
    while True:
        playsound('pedal_A.wav')

        #esperando que a pessoa reaperte a tecla A para assim parar a reprodução
        if keyboard.is_pressed("a"):
            print('Reprodução parada')
            break

rec_on_A()

