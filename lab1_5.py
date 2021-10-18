import math

x = int(input("Введите первый катет: "))
if x <= 0 :
    print("Катет не может быть меньше или равен 0")
while x <= 0 :
    x = int(input("Введите первый катет: "))
y = int(input("Введите второй катет: "))
if y <= 0 :
    print("Катет не может быть меньше или равен 0")
while y <= 0 :
    y = int(input("Введите второй катет: "))
else:
    import math

    Gep = math.sqrt(x ** 2 + y ** 2)

    print("Гипотинуза равна ", Gep)
    print("Площадь равна: ", x * y / 2)
    print("Периметр равен ", x + y + Gep)




