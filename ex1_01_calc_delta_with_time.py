import alg_ex_1
import sys
import time

orig_stdout = sys.stdout
f = open('ex1_01_module_time_output.txt', 'w')
sys.stdout = f

print(f'{time.ctime(time.time())}\n')

# Рекурсивная реализация алгоритма Евклида. --> GCD1 (n * e-06 = n / 10 ^ 6)
start1 = time.time()
alg_ex_1.gcd1(10000000, 90)
delta1 = (time.time() - start1)
print(f'Delta GCD1 (Recursion realization of Euclidean algorithm) = {delta1:.{10}}')

# Метод последовательного вычитания (классический) --> GCD2
start2 = time.time()
alg_ex_1.gcd2(10000000, 90)
delta2 = (time.time() - start2)
print(f'Delta GCD2 (Classic Euclidean algorithm) = {delta2:.{10}}')

if delta1 < delta2:
    print(f'\nGCD1 faster than GCD2 by {round(delta2 / delta1)} times!!!')
else:
    print(f'\nGCD2 faster than GCD1 by {round(delta1 / delta2)} times!!!')

sys.stdout = orig_stdout
f.close()