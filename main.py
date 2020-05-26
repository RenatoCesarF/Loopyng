import threading
import os

from sis_sec import pedais


#mostrando os pedais
pedais()

'''
--------------------------------------
Rodando todos os pedais ao mesmo tempo
--------------------------------------
'''


#exportando a função que faz tudo funcionar para o tkiner
def inicia_programa(nome_arquivo):
    os.system('py -3.7 {}'.format(nome_arquivo))
    # Ex: os.system('py -3.7 x.py')
if __name__ == "__main__":
    arquivos = ['rec_on_A.py','rec_on_S.py','rec_on_D.py','rec_on_F.py']
    processos = []
    for arquivo in arquivos:
        processos.append(threading.Thread(target=inicia_programa, args=(arquivo,)))
 
    #rodando os processos simultaneamente
    for processo in processos:
        processo.start()
  