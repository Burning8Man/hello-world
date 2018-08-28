# 6. В программе генерируется случайное целое число от 0 до 100. 
# Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться, больше или 
# меньше загаданного введенное пользователем число. Если за 10 
# попыток число не отгадано, то вывести его.

from random import random
n = round(random() * 100)
i = 1
print('The computer made a number from 0 to 100. Guess it. You have 10 attempts')
while i <= 10:
    u = int(input(str(i) + ' attempt: '))
    if u > n:
        print('Much')
    elif u < n:
        print('Few')
    else:
        print(f'You guessed the number on the {i} attempt!')
        break
    i += 1
else:
    print(f'You run out of 10 attempts. The correct answer is {n}')
