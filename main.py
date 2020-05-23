#importação das bibliotecas usadas
from time import sleep
from multiprocessing import Pool 
# importação das funções que gravam em determinado pedal
from rec_on_A import rec_on_A
from rec_on_S import rec_on_S
from rec_on_D import rec_on_D
from rec_on_F import rec_on_F

from sis_sec import pedais

# é necessário fazer essas funções rodarem todas ao mesmo
# temapo, porque do jeito que esta ele vai para a primeir
# e ai começar a segunda
# https://pt.stackoverflo w.com/questions/386595/python-executar-dois-scripts-ao-mesmo-tempo

pedais()

while True:
    rec_on_A()
    rec_on_S()
    rec_on_D()
    rec_on_F()