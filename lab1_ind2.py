import math
x = int(input("Введите число x: "))
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
if b == 0 :
    print("Число не может быть равно нулю")
while b == 0 :
    b = float(input("Введите число b: "))
else:
    Z = (x^2)/a + math.cos((x + b)^3)
print(Z)
