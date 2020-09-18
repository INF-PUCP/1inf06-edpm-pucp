class Nodo(object):
    def __init__(self, item):
        self._item = item
        self._next = None

class IteradorLista:
    def __init__(self, cabeza):
        self._actual = cabeza

    def __iter__(self):
        return self

    def __next__(self):
        if self._actual is None:
            raise StopIteration
        else:
            item = self._actual._item
            self._actual = self._actual._next
            return item

class Lista:
    # Contructor de lista vacia
    def __init__(self):
        self._head = None
        self._size = 0

    # Retorna numero de elementos en la lista
    def __len__(self):
        return self._size

    # Agregar un elemento a la lista
    def Agregar(self, item):
        nodo = Nodo(item)
        nodo._next = self._head;
        self._head = nodo
        self._size += 1

    # Determina si un elemento esta en la lista
    def __contains__(self, target):
        actual = self._head
        while actual is not None and actual._item != target:
            actual = actual._next
        return actual is not None

    # Elimina un elemento de la lista
    def Quitar(self, item):
        anterior = None
        actual = self._head
        while actual is not None and actual._item != item:
            anterior = actual;
            actual = actual._next;

        assert actual is not None, "El elemento no se encuentra en la lista."
        self._size -= 1
        if actual is self._head:
            self._head = actual._next
        else:
            anterior._next = actual._next
        return actual._item

    # Retorna un iterador para poder recorrer la lista
    def __iter__(self):
        return IteradorLista(self._head)

def main():
    lista = Lista()
    assert len(lista) == 0, "La lista debe ser vacia."

    lista.Agregar(15)
    assert len(lista) == 1, "La funcion Agregar falla."

    assert 15 in lista and not 13 in lista, "La funcion (__contains__) falla."

    lista.Agregar(17)
    lista.Agregar(15)
    lista.Agregar(13)
    assert lista.Quitar(15) == 15, "La funcion Quitar falla."
    assert lista.Quitar(15) == 15, "La funcion Quitar falla."

    try:
        lista.Quitar(15)
    except AssertionError:
        pass

    for item in lista:
        assert item == 17 or item == 13, "__iter__ falla."

    print("Todos los casos estan OK.")

if __name__ == "__main__":
    main()
