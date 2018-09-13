import random

N = 10


def sum_(m):
    s = 0
    while m > 0:
        s += m % 10
        m = m // 10
    return s


a = [0] * N
for i in range(N):
    a[i] = random.randrange(0, 50)
print(a)

for i in range(N - 1):
    for j in range(N - 1 - i):  # i in first loop is 0
        if sum_(a[j]) > sum_(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
a_result = []
for i in range(N):
    a_result.append(sum_(a[i]))
print(f'{a_result}')
