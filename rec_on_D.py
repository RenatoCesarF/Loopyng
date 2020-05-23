#esse código sera responsável por ouvir o teclado para que o mesmo
#funcione como controle da gravação e reprodução dos audios atraves
# da chamada das outras funções/arquivos.

#importação das bibliotecas usadas
import keyboard
from playsound import playsound
from time import sleep

#importação da função de gravação
from recording import record


#quando D for clicado chama a função de gravar no "pedal" D
def rec_on_D():

    #aguardando o pressionamento da letra 'D' 
    keyboard.wait('d')
    print('começando a gravar em...')
    sleep(1)
    print('\n 3...')
    sleep(1)
    print('\n 2...')
    sleep(1)
    print('\n 1...')

    record('pedal_D.wav')
    #função que realiza a gravação
    # Dentro da função record existe um if para caso a tecla D seja apertada 
    # novamente a gravação sera parada.
    # O parametro recebido é o nome do arquivo de audio

    #reproduzindo o audio gravado
    while True:
        playsound('pedal_D.wav')

        #esperando que a pessoa reaperte a tecla D para assim parar a reprodução
        if keyboard.is_pressed("d"):
            print('Reprodução parada')
            break
rec_on_D()