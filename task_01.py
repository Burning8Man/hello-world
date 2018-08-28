# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
#Числа и знак операции вводятся пользователем. После выполнения вычисления программа не 
#должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы 
#должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь 
#вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об 
#ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности 
#деления на ноль, если он ввел 0 в качестве делителя.

print('Enter a sign of operation (+, -, *, / or 0 for exit) and 2 integer digits')

operator = input('Please input an operator: ')
if operator != str(0):
  while operator != str(0):
    a = int(input('Please input first digit(a): '))
    b = int(input('Please input second digit(b): '))
    if operator == '+':
      sumab = a + b
      print(f'{a} + {b} = {sumab}')
      operator = input('Please input an operator: ')
      continue
    elif operator == '-':
      sub = a -b
      print(f'{a} - {b} = {sub}')
      operator = input('Please input an operator: ')
      continue
    elif operator == '*':
      mul = a * b
      print(f'{a} * {b} = {mul}')
      operator = input('Please input an operator: ')
      continue
    elif operator == '/':
      if b != 0:
        div = a / b
        print(f'{a} / {b} = {div}')
        operator = input('Please input an operator: ')
        continue
      else:
        print('ZeroDivision error. Try again!')
        operator = input('Please input an operator: ')
        continue
    else:
      print('Entered symbol is not allowed as operator')
      operator = input('Please input an operator: ')
      continue
  # print('GoodBye!!!')
else:
  print('GoodBye!!!')
  exit
