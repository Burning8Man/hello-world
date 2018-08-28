# 8. Посчитать, сколько раз встречается определенная цифра 
# в введенной последовательности чисел. Количество 
# вводимых чисел и цифра, которую необходимо посчитать, 
# задаются вводом с клавиатуры.

n = int(input('How many numbers will be there? '))
d = int(input('What figure count? '))
count = 0
for i in range(1,n+1):
    m = int(input("Number " + str(i) + ": "))
    while m > 0:
        if m%10 == d:
            count += 1
        m = m // 10
 
print(f'{count} digits {d} was introduced')