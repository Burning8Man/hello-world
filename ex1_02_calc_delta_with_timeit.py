from alg_ex_1 import gcd1, gcd2
import timeit
import sys
import time

orig_stdout = sys.stdout
f = open('ex1_02_module_timeit_output.txt', 'w')
sys.stdout = f

print(f'{time.ctime(time.time())}\n')

# С модулем timeit расчет времени работы алгоритма идёт очень медленно!!!

gcd1_t = timeit.timeit("gcd1(10000000, 9000)", setup="from __main__ import gcd1")
gcd2_t = timeit.timeit("gcd2(10000000, 9000)", setup="from __main__ import gcd2")

print(f'Delta GCD1 (Recursion realization of Euclidean algorithm) = \
{gcd1_t}')
print(f'Delta GCD2 (Classic Euclidean algorithm) = \
{gcd2_t}')


if gcd1_t < gcd2_t:
    print(f'\nGCD1 faster than GCD2 by {round(gcd2_t / gcd1_t)} times!!!')
else:
    print(f'\nGCD2 faster than GCD1 by {round(gcd1_t / gcd2_t)} times!!!')

sys.stdout = orig_stdout
f.close()