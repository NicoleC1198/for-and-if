import numpy as np

a = [2,3,4,5,6]
a_l = len(a)

for i in range(a_l):
    if a[i] < 3:
        f = a[i]
      #  print("valor menor a 3 es", f)
    
    elif a[i]==3:
        f1 = a[i]
      #  print("el valor equivalente es", f1)

    elif a[i] > 5:
        f3 = a[i]
       # print("este valor es mayor a 5 es", f3)

    else:
        f2 = a[i]
      #  print("este valor no es el if", f2)
    if a==1:
        print()