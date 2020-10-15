class Nodo:
    # Crear un nodo de arbol
    def __init__(self, valor, primogenito):
        self._valor = valor
        self._primogenito = primogenito
        self._hermano_derecho = None
    
    def _arbol(self):
       return Arbol(self)

class Bosque:
    # Crear un bosque vacio
    def __init__(self):
        self._nodo = None

    # Añadir un arbol al bosque
    def anadir_arbol(self, arbol):
        arbol._nodo._hermano_derecho = self._nodo
        self._nodo = arbol._nodo

    # Calcular longitud de un bosque
    def __len__(self):
        cur = self._nodo
        cnt = 0
        while not cur is None:
            cnt += 1
            cur = cur._hermano_derecho
        return cnt

    # Consultar i-esimo arbol en el bosque
    def __getitem__(self, indice):
        assert indice > 0, "Indice no valido"
        cur = self._nodo
        assert not cur is None, "Indice no valido"
        ind = 1
        while (cur and ind != indice):
            ind += 1
            cur = cur._hermano_derecho
        assert not cur is None, "Indice no valido"
        return cur._arbol()

class Arbol:
    # Plantar un arbol en el bosque
    def __init__(self, elemento, bosque = None):
        if bosque is None:
            self._nodo = elemento
        else:
            self._nodo = Nodo(elemento, bosque)

    # Consultar raiz de un arbol
    def raiz(self):
        return self._nodo._valor

    # Consultar la lista de hijos de un arbol
    def hijos(self):
        return self._nodo._primogenito

    # Calcular el numero de hijos de un arbol
    def numero_hijos(self):
        return len(self._nodo._primogenito)

    # Determina si un nodo es una hoja
    def es_hoja(self):
        return self.numero_hijos() == 0

def main():
    b1 = Bosque()
    assert len(b1) == 0, "Error en __len__"
    
    a1 = Arbol(10, b1)
    assert a1.raiz() == 10, "Error en raiz"
    assert len(a1.hijos()) == 0, "Error en hijos"
    assert a1.numero_hijos() == 0, "Error en numero_hijos"
    assert a1.es_hoja(), "Error en es_hoja"

    b1.anadir_arbol(a1)
    assert len(b1) == 1, "Error en __len__"

    a2 = Arbol(20, b1)
    assert a2.raiz() == 20, "Error en raiz"
    assert len(a1.hijos()) == 1, "Error en hijos"
    assert a1.numero_hijos() == 1, "Error en numero_hijos"
    assert not a1.es_hoja(), "Error en es_hoja"

    b3 = Bosque()
    a3 = Arbol(30, b3)
    b4 = Bosque()
    a4 = Arbol(40, b4)

    b5 = Bosque()
    b5.anadir_arbol(a3)
    assert len(b5) == 1, "Error en __len__"

    b5.anadir_arbol(a4)
    assert len(b5) == 2, "Error en __len__"

    a5 = Arbol(50, b5)
    assert a5.raiz() == 50, "Error en raiz"
    assert len(a5.hijos()) == 2, "Error en hijos de arbol"
    assert a5.numero_hijos() == 2, "Error en numero_hijos"
    assert not a5.es_hoja(), "Error en es_hoja"

    try:
        print(b5[0])
    except AssertionError:
        pass

    assert b5[1].raiz() == 40, "Error en anadir_arbol"
    assert b5[2].raiz() == 30, "Error en anadir_arbol"

    print("Todos los casos estan OK")

if __name__ == "__main__":
    main()
