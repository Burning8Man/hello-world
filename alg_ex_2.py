import math

# Решето Эратосфена

def Eratosthenes(n):
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b

# Решето Аткина

def Atkin(nmax):
    """
    Returns a list of prime numbers below the number "nmax"
    """
    is_prime = dict([(i, False) for i in range(5, nmax + 1)])
    for x in range(1, int(math.sqrt(nmax)) + 1):
        for y in range(1, int(math.sqrt(nmax)) + 1):
            n = 4 * x ** 2 + y ** 2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3 * x ** 2 + y ** 2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3 * x ** 2 - y ** 2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(nmax)) + 1):
        if is_prime[n]:
            ik = 1
            while (ik * n ** 2 <= nmax):
                is_prime[ik * n ** 2] = False
                ik += 1
    primes = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]:
            pass
        elif i in [2, 3] or is_prime[i]:
            primes.append(i)
        else:
            pass
    return primes

assert (Atkin(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


if __name__ == '__main__':
    print('Eratosthenes = ', Eratosthenes(10000))
    print('Atkin = ', Atkin(10000))
    if Eratosthenes(10000) == Atkin(10000):
        print('All primes the same!!! Excellent!!!')
    else:
        print('Something goes wrong(((!')