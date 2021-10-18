A1 = float(input("Введите A1:" ))
A2 = float(input("Введите A2:" ))
A3 = float(input("Введите A3:" ))
B1 = float(input("Введите B1:" ))
B2 = float(input("Введите B2:" ))
B3 = float(input("Введите B3:" ))
C1 = float(input("Введите C1:" ))
C2 = float(input("Введите C2:" ))
C3 = float(input("Введите C3:" ))
D1 = float(input("Введите D1:" ))
D2 = float(input("Введите D2:" ))
D3 = float(input("Введите D3:" ))
Opredelitel = A1 * B2 * C3 + B1 * C2 * A3 + C1 * A2 * B3 - C1 * B2 * A3 - A1 * C2 * B3 - B1 * A2 * C3
if Opredelitel == 0 :
    print("Определитель не может быть равен нулю")
else:
    Opredelitel1 = D1 * B2 * C3 + B1 * C2 * D3 + C1 * D2 * B3 - C1 * B2 * D3 - D1 * C2 * B3 - B1 * D2 * C3

    Opredelitel2 = A1 * D2 * C3 + D1 * C2 * A3 + C1 * A2 * D3 - C1 * D2 * A3 - A1 * C2 * D3 - D1 * A2 * C3

    Opredelitel3 = A1 * B2 * D3 + B1 * D2 * A3 + D1 * A2 * B3 - D1 * B2 * A3 - A1 * D2 * B3 - B1 * A2 * D3
    x = Opredelitel1 / Opredelitel

    y = Opredelitel2 / Opredelitel

    z = Opredelitel3 / Opredelitel

    print ('X равен: ', (x))
    print('Y равен: ', (y))
    print('Z равен: ', (z))

