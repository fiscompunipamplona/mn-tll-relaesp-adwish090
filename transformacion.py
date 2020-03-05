import math

c=3e8     #m/s

x=input("Escriba la distancia en años luz")
x=float(x)    #ly

ly=x*9.461e15

v=input ("Escriba la velocidad")
v=float(v)    #m/s

vel=v/c       #m/s

fac=1/math.sqrt(1-((vel**2)/(c**2)))

print("El tiempo desde la Tierra es:")
t=ly/vel #s
print(t)

print("El tiempo desde la nave es:")
tl=((t-((vel*ly)/(c*c))))*fac  #s
print(tl)

