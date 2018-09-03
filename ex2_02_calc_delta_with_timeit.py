from alg_ex_2 import Eratosthenes, Atkin
import timeit
import sys
import time

orig_stdout = sys.stdout
f = open('ex2_02_module_timeit_output.txt', 'w')
sys.stdout = f

print(f'{time.ctime(time.time())}\n')

# С модулем timeit расчет времени работы алгоритма идёт очень медленно!!!

eratosthenes_t = timeit.timeit("Eratosthenes(30)", setup="from __main__ import Eratosthenes")
atkin_t = timeit.timeit("Atkin(30)", setup="from __main__ import Atkin")

print(f'Delta Eratosthenes algorithm = \
{eratosthenes_t}')
print(f'Delta Atkin algorithm = \
{atkin_t}')


if eratosthenes_t < atkin_t:
    print(f'\nEratosthenes algorithm faster than Atkin algorithm by {round(atkin_t / eratosthenes_t)} times!!!')
else:
    print(f'\nAtkin algorithm faster than Eratosthenes algorithm by {round(eratosthenes_t / atkin_t)} times!!!')

sys.stdout = orig_stdout
f.close()
