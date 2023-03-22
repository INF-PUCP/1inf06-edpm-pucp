class Arbol:
    def __init__(self, item = None, izq = None, der = None):
        self._item = item
        self._izquierda = izq
        self._derecha = der

    def Vacio(self):
        return self._item is None

    def Raiz(self):
        assert not self.Vacio(), "Error: Arbol vacio"
        return self._item

    def Izquierda(self):
        assert not self.Vacio(), "Error: Arbol vacio"
        return self._izquierda

    def Derecha(self):
        assert not self.Vacio(), "Error: Arbol vacio"
        return self._derecha

    def Altura(self):
        if self.Vacio():
            return 0
        altura_izquierda = 0 if self._izquierda is None else self._izquierda.Altura()
        altura_derecha = 0 if self._derecha is None else self._derecha.Altura()
        return 1 + max(altura_izquierda, altura_derecha)
    def Count(self):
        if self.Vacio():
            return 0
        cnt_izquierda = 0 if self._izquierda is None else self._izquierda.Count()
        cnt_derecha = 0 if self._derecha is None else self._derecha.Count()
        return 1 + cnt_izquierda + cnt_derecha

def main():
    a1 = Arbol()
    assert a1.Vacio(), "Error en Vacio"
    try:
        a1.Izquierda()
    except AssertionError:
        pass

    try:
        a1.Raiz()
    except AssertionError:
        pass

    try:
        a1.Derecha()
    except AssertionError:
        pass

    assert a1.Altura() == 0, "Error en Altura"
    assert a1.Count() == 0, "Error en Count"

    a2 = Arbol(7)
    a3 = Arbol(9)

    assert not a2.Vacio(), "Error en Vacio"
    assert not a3.Vacio(), "Error en Vacio"
    assert a2.Raiz() == 7, "Error en Raiz"
    assert a2.Derecha() is None, "Error en Derecha"
    assert a2.Count() == 1, "Error en Count"

    a4 = Arbol(3, a2)
    assert not a4.Vacio(), "Error en Vacio"
    assert a4.Izquierda() is a2, "Error en Izquierda"
    assert a4.Raiz() == 3, "Error en Raiz"
    assert a4.Derecha() is None, "Error en Derecha"
    assert a4.Altura() == 2, "Error en Altura"
    assert a4.Count() == 2, "Error en Count"
    
    a5 = Arbol(5, None, a3)
    assert not a5.Vacio(), "Error en Vacio"
    assert a5.Izquierda() is None, "Error en Izquierda"
    assert a5.Raiz() == 5, "Error en Raiz"
    assert a5.Derecha() == a3, "Error en Derecha"
    assert a5.Altura() == 2, "Error en Altura"
    assert a5.Count() == 2, "Error en Count"

    a6 = Arbol(11, a2, a3)
    assert not a6.Vacio(), "Error en Vacio"
    assert a6.Izquierda() is a2, "Error en Izquierda"
    assert a6.Raiz() == 11, "Error en Raiz"
    assert a6.Derecha() is a3, "Error en Derecha"
    assert a6.Altura() == 2, "Error en Altura"
    assert a6.Count() == 3, "Error en Count"
    
    a7 = Arbol(13, a6, a5)
    assert a7.Altura() == 3, "Error en Altura"
    assert a7.Count() == 6, "Error en Count"
    
    a8 = Arbol(15, a7, None)
    assert a8.Altura() == 4, "Error en Altura"
    assert a8.Count() == 7, "Error en Count"

    print("Todos los casos estan OK")

if __name__ == "__main__":
    main()
