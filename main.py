# Считываем значение Х
X = int(input())

# Вычисляем количество часов и минут
hours = X // 60
minutes = X % 60

# Выводим время сигнала на будильнике
print(hours)
print(minutes)
