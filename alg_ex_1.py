# Алгоритм Евклида. Нахождение "Наибольшего Общего Делителя (НОД)"

# Рекурсивная реализация алгоритма Евклида. --> GCD1
# Euclidean algorithm. An efficient method for computing the greatest common divisor (GCD).

def gcd1(a, b):
    if b == 0:
        return a
    else:
        return gcd1(b, a % b)

if __name__ == '__main__':
    a = int(input('Please enter the 1st argument: '))
    b = int(input('Please enter the 2nd argument: '))
    print(gcd1(a, b))

# Метод последовательного вычитания (классический) --> GCD2
# import sys
#
# sys.setrecursionlimit(2000)

def gcd2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

if __name__ == '__main__':
    a = int(input('Please enter the 1st argument: '))
    b = int(input('Please enter the 2nd argument: '))
    print(gcd2(a, b))

