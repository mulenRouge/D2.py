# Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

x = int(input('Введите число x: '))
y = int(input('Введите число y: ')) 
if y > x:
    for i in range(x, y):
            if i % 2==0 and i % 3==0:
                print(i)
    if y < x:
        for i in range(y, x):
            if i % 2==0 and i % 3==0:
                print(i)
