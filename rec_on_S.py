#esse código sera responsável por ouvir o teclado para que o mesmo
#funcione como controle da gravação e reprodução dos audios atraves
# da chamada das outras funções/arquivos.

#importação das bibliotecas usadas
from playsound import playsound
from pynput.keyboard import Key, Listener
import keyboard
from time import sleep

#importação da função de reprodução
from recording import record


#quando S for clicado chama a função de gravar no pedal S
def rec_on_S():

    #aguardando o pressionamento da letra 'S'
    keyboard.wait('S')
    print('começando a gravar em...')
    sleep(1)
    print('\n 3...')
    sleep(1)
    print('\n 2...')
    sleep(1)
    print('\n 1...')


    record('pedal_S.wav')
    #função que realiza a gravação
    # Dentro da função record existe um if para caso a tecla S seja apertada 
    # novamente a gravação sera parada.
    # O parametro recebido é o nome do arquivo de audio 

    #reproduzindo o audio gravado
    while True:

        #preciso mandar o nome do arquivo de cá para la,
        playsound('pedal_S.wav')
        
        #esperando que a pessoa reaperte a tecla S para assim parar a reprodução
        if keyboard.is_pressed("s"):
            print('Reprodução parada')
            break

rec_on_S()