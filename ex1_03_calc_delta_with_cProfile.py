import cProfile
from alg_ex_1 import gcd1, gcd2
import sys
import time

orig_stdout = sys.stdout
f = open('ex1_03_cProfile_output.txt', 'w')
sys.stdout = f

print(f'{time.ctime(time.time())}\n')

# При запуске вывод программы автоматически сохранятся в cProfile_output.txt

def main_gcd1():
    gcd1_t = gcd1(10000000, 90)

def main_gcd2():
    gcd1_t = gcd2(10000000, 90)

print('Recursion realization of Euclidean algorithm:\n')
cProfile.run('main_gcd1()')
print('Classic realization of Euclidean algorithm:\n')
cProfile.run('main_gcd2()')

sys.stdout = orig_stdout
f.close()