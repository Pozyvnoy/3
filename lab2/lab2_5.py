n = float(input("n = "))
for x in range(n + 1):
    for y in range(n + 1):
         if (x*x+y*y)==n :
            print(x,y)
            print(y,x)