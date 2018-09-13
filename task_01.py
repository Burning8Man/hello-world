import random

N = 10

a = [0] * N
for i in range(N):
    a[i] = random.randrange(-100, 100)
print(f'raw_list = {a}')

for i in range(N - 1):
    # print('#' * 66)
    # print(i)
    for j in range(N - 1 - i):
        # print('*' * 66)
        # print(j)
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(f'sorted a = {a}')
a_reverse = sorted(a, reverse=True)
print(f'sorted and reversed = {a_reverse}')
