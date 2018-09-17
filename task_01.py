"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке. Для решения задачи рекомендую
воспользоваться алгоритмом sha1 из модуля hashlib или встроенной в python функцией hash().
"""
import string
import random

X = 26
Y = 1000
SUBSTRING = 'xx'

# ht_no_repetitions = ''.join(random.sample(string.ascii_lowercase, X))
# print(ht_no_repetitions)

ht_with_repetitions = ''.join(random.choice(string.ascii_lowercase) for y in range(Y))
print(f'ht_with_repetitions = {ht_with_repetitions}')

class Hash:
    def __init__(self, string, size):
        self.str = string
        self.hash = 0

        for i in range(0, size):
            self.hash += ord(self.str[i])

        self.init = 0
        self.end = size

    def update(self):
        if self.end <= len(self.str) - 1:
            self.hash -= ord(self.str[self.init])
            self.hash += ord(self.str[self.end])
            self.init += 1
            self.end += 1

    def digest(self):
        return self.hash

    def text(self):
        return self.str[self.init:self.end]


def rabin_karp_matcher(substring, string):
    if substring == None or string == None:
        return print('Substring or string is None')
    if substring == '' or string == '':
        return print('Substring or string is ""')

    if len(substring) > len(string):
        return print('The length of substring > the length of string')

    hs = Hash(string, len(substring))
    hsub = Hash(substring, len(substring))
    hsub.update()

    for i in range(len(string) - len(substring) + 1):
        if hs.digest() == hsub.digest():
            if hs.text() == substring:
                return i
        hs.update()

    return print(f'ERR: The substring "{SUBSTRING}" is not found in the string!')


rkm = rabin_karp_matcher(SUBSTRING, ht_with_repetitions)

print(rkm)
print(ht_with_repetitions[rkm : rkm + 2])
