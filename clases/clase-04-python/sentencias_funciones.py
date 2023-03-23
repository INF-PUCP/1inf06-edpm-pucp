pass # No se hace nada
b = 10
a = 2 ** b
print(a)

x, y, z = 0, 1, 2
# las asignaciones se hacen simultaneamente
# no secuencialmente
x, y, z = x + 5, x + y, x + y + z
print(x, y, z)

x, y = 10, 20
print((x, y)[0])

x, y = [10, 20]
print(x)
print(y)

x, y = 'Hi'
print(x)
print(y)

point = 10, 20, 30
print(point)
print(type(point))

x = int(input("Ingrese un entero: "))
if x < 0:
    x = 0
    print("Negativo cambiado a cero.")
elif x == 0:
    print("Cero.")
elif x == 1:
    print("Unitario.")
else:
    print("Mas grande.")

# Fibonaci
n = int(input("Ingrese que fibonacci desea: "))
if n < 0:
    n = 0
    print("Negativo cambiado a cero.")
print("Fibonacci " + str(n) + ": ", end="")
if n == 0:
    print(1)
elif n == 1:
    print(1)
else:
    f0 = 1
    f1 = 1
    for i in range(2, n + 1):
        f0, f1 = f1, f0 + f1
    print(f1)

for i in range(5):
    print(i)
for i in range(5, 10):
    print(i)
for i in range(0, 10, 3):
    print(i)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(str(n) + " = " + str(x) + " * " + str(n // x))
            break
    else:
        print(str(n) + " es primo.")

r = input("Cual es tu nombre? ")

def fibonacci(n):
    f0, f1 = 1, 1
    if n < 2:
        return 1
    else:
        for i in range(2, n + 1):
            f0, f1 = f1, f0 + f1
        return f1

f = fibonacci
print(f(100))

def fibonacci_lista(n):
    f0, f1 = 1, 1
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        resultado = [1, 1]
        for i in range(2, n + 1):
            f0, f1 = f1, f0 + f1
            resultado.append(f1)
        return resultado

f2 = fibonacci_lista
print(f2(10))
