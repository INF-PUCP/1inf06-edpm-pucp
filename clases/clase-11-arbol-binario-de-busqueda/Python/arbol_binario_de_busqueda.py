class Arbol:
    # Crear un arbol vacio
    def __init__(self, raiz = None):
        self._raiz = raiz

    @classmethod
    def plantar(cls, izquierda, elemento, derecha):
        assert ((izquierda.vacio() or elemento > izquierda.maximo()) and\
                (derecha.vacio() or elemento < derecha.minimo())),\
                "No podemos plantar"
        _raiz = Nodo(elemento)
        _raiz._izquierda = izquierda
        _raiz._derecha = derecha
        return cls(_raiz)

    # Deteminar si el arbol es vaio
    def vacio(self):
        return self._raiz is None

    # Insertar un elemento
    def insertar(self, elemento):
        if self.vacio():
            self._raiz = Nodo(elemento)
        else:
            if elemento == self._raiz._valor:
                pass
            elif elemento < self._raiz._valor:
                self._raiz._izquierda.insertar(elemento)
            else:
                self._raiz._derecha.insertar(elemento)

    # Determinar si un elemento pertenece al arbol
    def pertenece(self, elemento):
        if self.vacio():
            return False
        if elemento == self._raiz._valor:
            return True
        if elemento < self._raiz._valor:
            return self._raiz._izquierda.pertenece(elemento)
        return self._raiz._derecha.pertenece(elemento)

    # Consultar el menor elemento
    def minimo(self):
        assert not self.vacio(), "Arbol vacio"
        if self._raiz._izquierda.vacio():
            return self._raiz._valor
        return self._raiz._izquierda.minimo()

    # Consultar el mayor elemento
    def maximo(self):
        assert not self.vacio(), "Arbol vacio"
        if self._raiz._derecha.vacio():
            return self._raiz._valor
        return self._raiz._derecha.maximo()

    # Eliminar un elemento
    def eliminar(self, elemento):
        if self.vacio():
            return
        if (elemento == self._raiz._valor and self._raiz._derecha.vacio()):
            self._raiz = self._raiz._izquierda._raiz
            return
        if (elemento == self._raiz._valor and self._raiz._izquierda.vacio()):
            self._raiz = self._raiz._derecha._raiz
            return
        if (elemento == self._raiz._valor and not self._raiz._izquierda.vacio() and not self._raiz._derecha.vacio()):
            nueva_derecha = self._raiz._derecha
            minimo_derecha = nueva_derecha.minimo()
            nueva_derecha.eliminar(minimo_derecha)
            arbol = Arbol.plantar(self._raiz._izquierda, minimo_derecha, nueva_derecha)
            self._raiz = arbol._raiz
            return
        if elemento < self._raiz._valor:
            nueva_izquierda = self._raiz._izquierda
            nueva_izquierda.eliminar(elemento)
            arbol = Arbol.plantar(nueva_izquierda, self._raiz._valor, self._raiz._derecha)
            self._raiz = arbol._raiz
        else:
            nueva_derecha = self._raiz._derecha
            nueva_derecha.eliminar(elemento)
            arbol = Arbol.plantar(self._raiz._izquierda, self._raiz._valor, nueva_derecha)
            self._raiz = arbol._raiz

    # Recorrer el arbol en preorden
    def preorden(self):
        if self._raiz is None:
            return []
        return self._raiz._izquierda.preorden() + [self._raiz._valor] + self._raiz._derecha.preorden()

class Nodo(object):
    def __init__(self, elemento):
        self._valor = elemento
        self._izquierda = Arbol()
        self._derecha = Arbol()

def main():
    arbol = Arbol()
    assert arbol.vacio(), "Error en vacio()"

    try:
        arbol.minimo()
    except AssertionError:
        pass

    try:
        arbol.maximo()
    except AssertionError:
        pass

    arbol.insertar(10)
    assert not arbol.vacio(), "Error en insertar()"
    assert arbol.pertenece(10), "Error en pertenece()"
    assert not arbol.pertenece(20), "Error en pertenece()"
    assert arbol.minimo() == 10, "Error en minimo()"
    assert arbol.maximo() == 10, "Error en maximo()"

    arbol.insertar(5)
    arbol.insertar(20)
    assert not arbol.vacio(), "Error en insertar()"
    assert arbol.pertenece(10), "Error en pertenece()"
    assert arbol.pertenece(5), "Error en pertenece()"
    assert arbol.pertenece(20), "Error en pertenece()"
    assert arbol.minimo() == 5, "Error en minimo()"
    assert arbol.maximo() == 20, "Error en maximo()"

    arbol2 = Arbol()
    arbol3 = Arbol()
    arbol4 = Arbol.plantar(b, 40, c)
    assert not arbol4.vacio(), "Error en plantar()"
    assert arbol4.pertenece(40), "Error en plantar()"
    assert arbol4.minimo() == 40, "Error en minimo()"
    assert arbol4.maximo() == 40, "Error en maximo()"

    try:
        arbol5 = Arbol.plantar(arbol4, 30, arbol3)
    except AssertionError:
        pass

    try:
        arbol5 = Arbol.plantar(arbol2, 50, arbol4)
    except AssertionError:
        pass

    arbol5 = Arbol.plantar(arbol, 30, arbol3)
    assert not arbol5.vacio(), "Error en plantar()"
    assert arbol5.pertenece(30), "Error en plantar()"
    assert arbol5.pertenece(5), "Error en plantar()"
    assert arbol5.pertenece(10), "Error en plantar()"
    assert arbol5.pertenece(20), "Error en plantar()"
    assert arbol5.minimo() == 5, "Error en plantar()"
    assert arbol5.maximo() == 30, "Error en plantar()"

    arbol6 = Arbol.plantar(arbol2, 30, arbol4)
    assert not arbol6.vacio(), "Error en plantar()"
    assert arbol6.pertenece(30), "Error en plantar()"
    assert arbol6.pertenece(40), "Error en plantar()"
    assert arbol6.minimo() == 30, "Error en plantar()"
    assert arbol6.maximo() == 30, "Error en plantar()"

    arbol7 = Arbol.plantar(arbol, 30, arbol4)
    assert not arbol7.vacio(), "Error en plantar()"
    assert arbol7.pertenece(30), "Error en plantar()"
    assert arbol7.pertenece(5), "Error en plantar()"
    assert arbol7.pertenece(10), "Error en plantar()"
    assert arbol7.pertenece(20), "Error en plantar()"
    assert arbol7.pertenece(40), "Error en plantar()"
    assert arbol7.minimo() == 5, "Error en plantar()"
    assert arbol7.maximo() == 40, "Error en plantar()"

    arbol2.eliminar(999)
    assert arbol2.vacio(), "Error en eliminar()"

    arbol4.eliminar(40)
    assert arbol4.vacio(), "Error en eliminar()"

    arbol4 = Arbol.plantar(arbol2, 40, arbol3)
    arbol6 = Arbol.plantar(arbol2, 30, arbol4)
    arbol7 = Arbol.plantar(arbol, 30, arbol4)

    arbol7.eliminar(30)
    assert arbol7.pertenece(40), "Error en eliminar()"
    assert arbol7.minimo() == 40, "Error en eliminar()"
    assert arbol7.maximo() == 40, "Error en eliminar()"
