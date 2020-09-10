a = ['spam', 'eggs', 100, 1234]
print(a)
print(a[0])
print(a[3])
print(a[-1]) # ultimo
print(a[-2]) # penultimo

print(a[0:2])
print(a[:2])
print(a[2:2])
print(a[2:4])
print(a[-0]) # lo mismo que cero
print(a[::2]) # lista[inicio:fin:paso]

print(type(a))
print(len(a))
print(type(len))
print(type(len(a)))

# bucles
for item in a:
    print(item)

# estamos realizando una asignacion multiple
for index, item in enumerate(a):
    print(index, item)

print(type(enumerate(a)))
print(enumerate(a))
print(list(enumerate(a)))

for index, item in enumerate(a, start = 1):
    print(index, item)

print(a[:2] + ['bacon', 2 * 2]) # lista concatenada
print(3 * a[:3] + ['GAAA'])
a[2] = a[2] + 23 # las listas son mutables
print(a)

a[1:1] = ['bletch', 'xyzzy'] # insertar sin reemplazar
print(a)
a[:0] = a # de acuerdo a lo anterior, estaria duplicando
print(a)

estaciones = ['primavera', 'verano', 'otogno', 'invierno']
print(estaciones)
print(list(enumerate(estaciones, start = 69)))

print([i for i in range(7)])
print([0 for i in range(7)])

lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
lista3 = [lista1, lista2]
print(lista3)
print(lista3[0][1])

estaciones.sort()
print(estaciones)
estaciones[0] = 'Invierno'
estaciones.sort()
print(estaciones)

lista4 = [5, 2, 3, 1, 4]
lista4.sort()
print(lista4)
lista4.sort(reverse = True)
print(lista4)

oracion = "Viktor Khlebnikov es el profesor de Estructura de Datos y Programacion Metodica"
print(oracion.split())
print(sorted(oracion.split(), key = str.lower))

print(max(0, 100, -400))
print(max("C", "C++", "Java", "Python"))

# Da error porque no esta definida la comparacion entre int y str
# experimento = ['Z', 67, 'a', ("Hola mundo", 69)]
#print(experimento.sort())
