import sys
# import ctypes
# import struct
from task_01_1 import eratosthenes
from task_01_2 import atkin
import time

orig_stdout = sys.stdout
f = open('show_case.txt', 'w')
sys.stdout = f

print(f'{time.ctime(time.time())}\n')


def show_case(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_case(y, level + 1)
        elif not isinstance(x, str):
            for y in x:
                show_case(y, level + 1)


print('#' * 100)
show_case(eratosthenes(10000))
print('#' * 100)
show_case(atkin(10000))
print('#' * 100)

# LLLLLLl ->структуры целого типа
# print(ctypes.string_at(id(x), sys.getsizeof(x)))
# print(struct.unpack('LLLLLLl', ctypes.string_at(id(x), sys.getsizeof(x))))
# print(id(int))

sys.stdout = orig_stdout
f.close()
