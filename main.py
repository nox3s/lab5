#Задание 1
#поключаем библиотеку math
"""import math
#выводим заголовок таблицы
print(f"{'x':>8} {'sin(x)':>10}")
print("-" * 20)
#перебераем значения x и вычисляем sin(x)
for i in range(11) :
    x = i * math.pi / 10
    y = math.sin(x)
    print(f"{x:8.4f} {y:10.4f}") #вывод результатов с форматированием
"""

#Задание 2
#ввод данных
n = int(input("Введите N: "))
#инициализация переменных
sum_num = 0
product = 1
sum_squares = 0
#перебор чисел от 1 до N
for i in range(1, n + 1):
    sum_num += i
    product *= i
    sum_squares += i ** 2
#вывод результатов
print(f"Сумма: {sum_num}")
print(f"Произведение: {product}")
print(f"Сумма квадратов: {sum_squares}")