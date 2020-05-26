'''

Até o momento esse arquivo ainda não é usado, é preciso
concertar a função de gravação para ai chama-la aqui e
tudo voltar ao normal

Na parte de reprodução do audio gravado, não será mais 
usado playsound() mas sim a futura função do TK_play

'''
#importação das bibliotecas
from time import sleep
from playsound import playsound
import keyboard

#importando a função de gravação
from TK_record import record


#quando A for clicado chama a função de gravar no "pedal" A
def pedal_A():
    #esse print aparecera no seu terminal caso a função seja chamada
    print('Ativado pedal A')

    #função de gravação:

    
    #reproduzindo o audio gravado                                                                                                                                     
    while True:
        playsound('pedal_A.wav')