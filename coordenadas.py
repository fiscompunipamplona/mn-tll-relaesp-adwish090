import math as mt

r=input("Asigne un valor para r")
r=float(r)

ang=input("Asigne un valor para el angulo")
ang=float(ang)

c=((mt.pi*ang)/180)

z=input("Asigne un valor para z")
z=float(z)

print("El resultado en el eje x es:")
x=r*(mt.cos(c))
print(x)

print("El resultado en el eje y es:")
y=r*(mt.sin(c))
print (y)

print("El resultado en el eje z es:")
print (z)


