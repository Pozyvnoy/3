chislo = int(input("Введите целое: "))
mult = 1
while (chislo != 0):
    mult = mult * (chislo % 10)
    chislo = chislo // 10
print("Произведение цифр равно: ", mult)