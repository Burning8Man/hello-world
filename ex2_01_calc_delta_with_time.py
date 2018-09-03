import alg_ex_2
import sys
import time

orig_stdout = sys.stdout
f = open('ex2_01_module_time_output.txt', 'w')
sys.stdout = f

print(f'{time.ctime(time.time())}\n')

# Решето Эратосфена
start1 = time.time()
alg_ex_2.Eratosthenes(100000)
delta1 = (time.time() - start1)
print(f'Eratosthenes(n) algorithm delta = {delta1:.{10}}')

# Решето Аткина
start2 = time.time()
alg_ex_2.Atkin(100000)
delta2 = (time.time() - start2)
print(f'Atkin(nmax) algorithm delta = {delta2:.{10}}')

if delta1 < delta2:
    print(f'\nEratosthenes algorithm faster than Atkin algorithm by {round(delta2 / delta1)} times!!!')
else:
    print(f'\nAtkin algorithm faster than Eratosthenes algorithm by {round(delta1 / delta2)} times!!!')

sys.stdout = orig_stdout
f.close()
