# 2. Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

print('<Please input an integer number>')
num = int(input('>> '))
even = odd = 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f'Number of even digits are(is) {even}\nNumber of odd digits are(is) {odd}')