"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
# int(num, 16)  # back convert to decimal
# hex(num)  # forward convert to hexadecimal notation
num1_raw = hex(int(input('Please enter the 1-st number in hexadecimal notation: '), 16)).upper()[2:]
num2_raw = hex(int(input('Please enter the 2-nd number in hexadecimal notation: '), 16)).upper()[2:]

num1_list = []
for num1 in str(num1_raw):
    num1_list.append(num1)
print(f'\n1-st entered number in hexadecimal notation is: {num1_list}')

num2_list = []
for num2 in str(num2_raw):
    num2_list.append(num2)
print(f'2-nd entered number in hexadecimal notation is: {num2_list}')

sum_num = hex(int(num1_raw, 16) + int(num2_raw, 16)).upper()[2:]
sum_num_list = []
for sum_ in str(sum_num):
    sum_num_list.append(sum_)
print(f'\nSum of 2 entered numbers in hexadecimal notation is: {sum_num_list}')

mul_num = hex(int(num1_raw, 16) * int(num2_raw, 16)).upper()[2:]
mul_num_list = []
for mul_ in str(mul_num):
    mul_num_list.append(mul_)
print(f'Mult of 2 entered numbers in hexadecimal notation is: {mul_num_list}')
