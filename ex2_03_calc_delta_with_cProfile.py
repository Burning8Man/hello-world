import cProfile
from alg_ex_2 import Eratosthenes, Atkin
import sys
import time

orig_stdout = sys.stdout
f = open('ex2_03_cProfile_output.txt', 'w')
sys.stdout = f

print(f'{time.ctime(time.time())}\n')

# При запуске программы вывод автоматически сохранятся в ex2_03_cProfile_output.txt

def main_eratosthenes():
    eratosthenes_t = Eratosthenes(100000)

def main_atkin():
    atkin_t = Atkin(100000)

print('Eratosthenes algorithm:\n')
cProfile.run('main_eratosthenes()')
print('Atkin algorithm:\n')
cProfile.run('main_atkin()')

sys.stdout = orig_stdout
f.close()