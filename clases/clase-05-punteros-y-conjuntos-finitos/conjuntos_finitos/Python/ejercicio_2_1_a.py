def ConjuntoVacio():
    return []

def ConjuntoUnitario(elemento):
    return [elemento]

def EsConjuntoVacio(conjunto):
    return conjunto == []

def Pertenece(elemento, conjunto):
    return elemento in conjunto

def Agregar(elemento, conjunto):
    conjunto.append(elemento)
    return conjunto

def Quitar(elemento, conjunto):
    nuevo = [item for item in conjunto if item != elemento]
    return nuevo

def Union(conjunto1, conjunto2):
    resultado = []
    for elemento in conjunto1:
        resultado.append(elemento)
    for elemento in conjunto2:
        resultado.append(elemento)
    return resultado

def Interseccion(conjunto1, conjunto2):
    resultado = []
    for actual in conjunto1:
        if Pertenece(actual, conjunto2):
            resultado.append(actual)
    return resultado

def Diferencia(conjunto1, conjunto2):
    resultado = []
    for actual in conjunto1:
        if not Pertenece(actual, conjunto2):
            resultado.append(actual)
    return resultado

def Cardinalidad(conjunto):
    conjunto = list(set(conjunto))
    return len(conjunto)

def main():
    conjunto1 = ConjuntoVacio()
    assert conjunto1 == [], "Error de la funcion ConjuntoVacio."

    conjunto2 = ConjuntoUnitario(13);
    conjunto3 = ConjuntoUnitario(25);
    assert conjunto2 == [13] and conjunto3 == [25], "Error de la funcion ConjuntoUnitario."

    assert EsConjuntoVacio(conjunto1) and not EsConjuntoVacio(conjunto2), "Error de la funcion EsConjuntoVacio."

    assert Pertenece(13, conjunto2) and not Pertenece(13, conjunto3), "Error de la funcion Pertenece."

    assert Agregar(15, conjunto2) == [13, 15], "Error de la funcion Agregar."
    assert Agregar(17, conjunto2) == [13, 15, 17], "Error de la funcion Agregar."
    assert Agregar(15, conjunto2) == [13, 15, 17, 15], "Error de la funcion Agregar."

    conjunto2 = Quitar(15, conjunto2)
    assert conjunto2 == [13, 17], "Error de la funcion Quitar."
    conjunto2 = Quitar(15, conjunto2)

    conjunto2 = Union(conjunto2, conjunto3)
    assert conjunto2 == [13, 17, 25], "Error de la funcion Union."

    conjunto2 = Interseccion(conjunto2, conjunto3)
    assert conjunto2 == [25], "Error de la funcion Interseccion."

    conjunto2 = Agregar(11, conjunto2)
    conjunto2 = Diferencia(conjunto2, conjunto3)
    assert conjunto2 == [11], "Error de la funcion Diferencia."

    conjunto2 = Agregar(11, conjunto2)
    assert Cardinalidad(conjunto2) == 1, "Error de la funcion Cardinalidad."

    print("Todos los casos estan OK,")

if __name__ == "__main__":
    main()
