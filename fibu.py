import math as mt 

print ("La serie de Fibunacci hasta 1000 es:")

f1=1
f2=2
print(f1)
print(f2)

f3=f1+f2

print(f3)

while f1<1000:
    f1=f2
    f2=f3
    f3=f1+f2
    if f3>1000:
        break
    print(f3)


