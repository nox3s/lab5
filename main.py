#поключаем библиотеку math
import math
#выводим заголовок таблицы
print(f"{'x':>8} {'sin(x)':>10}")
print("-" * 20)
#перебераем значения x и вычисляем sin(x)
for i in range(11) :
    x = i * math.pi / 10
    y = math.sin(x)
    print(f"{x:8.4f} {y:10.4f}") #вывод результатов с форматированием