class Lista:
    # Crea lista vacia o con un elemento
    def __init__(self, elemento = None):
        if elemento is None:
            self._longitud = 0
            self._head = self._tail = None
        else:
            nodo = Nodo(elemento)
            self._longitud = 1
            self._head = self._tail = nodo

    # True si la lista es vacia
    def EsVacia(self):
        return self._head is None

    # Longitud de la lista
    def __len__(self):
        return self._longitud

    # Añadir elemento por la izquierda
    def AgregarIzquierda(self, elemento):
        nodo = Nodo(elemento)
        if self.EsVacia():
            self._tail = nodo
        else:
            nodo._next = self._head
            self._head._prev = nodo
        self._head = nodo
        self._longitud += 1

    # añadir elemento por la derecha
    def AgregarDerecha(self, elemento):
        nodo = Nodo(elemento)
        if self.EsVacia():
            self._head = nodo
        else:
            nodo._prev = self._tail
            self._tail._next = nodo
        self._tail = nodo
        self._longitud += 1

    # Devuelve el elemento mas a la izquierda de la lista
    def Head(self):
        assert not self.EsVacia(), "La lista esta vacia."
        return self._head._valor

    # Devuelve el elemento mas a la derecha de la lista
    def Tail(self):
        assert not self.EsVacia(), "La lista esta vacia."
        return self._tail._valor

    # Eliminar el elemento mas a la derecha de la lista
    def EliminarDerecha(self):
        assert not self.EsVacia(), "La lista esta vacia."
        self._tail = self._tail._prev
        if self._tail is None:
            self._head = None
        else:
            self._tail._next = None

        self._longitud -= 1
    
    # Eliminar el elemento mas a la izquierda de la lista
    def EliminarIzquierda(self):
        assert not self.EsVacia(), "La lista esta vacia."
        self._head = self._head._next
        if self._head is None:
            self._tail = None
        else:
            self._head._prev = None
        self._longitud -= 1

    def Concatenar(self, otra):
        lista = Lista()
        actual = self._head
        while actual is not None:
            lista.AgregarDerecha(actual._valor)
            actual = actual._next
        actual = otra._head
        while actual is not None:
            lista.AgregarDerecha(actual._valor)
            actual = actual._next
        return lista

    def Recorrer(self):
        actual = self._head
        while actual is not None:
            print(actual._valor, end = " ")
            actual = actual._next
        print()

    def RecorrerReverso(self):
        actual = self._tail
        while actual is not None:
            print(actual._valor, end = " ")
            actual = actual._prev
        print()

    def __contains__(self, target):
        actual = self._head
        while actual is not None and actual._valor != target:
            actual = actual._next
        return actual is not None

    def __iter__(self):
        return DoubleLinkedListIterator(self._head)

# Clase privada para creacion de nodos de la lista
class Nodo(object):
    def __init__(self, elemento):
        self._valor = elemento
        self._next = None
        self._prev = None

# Define el iterador para la lista doblemente enlazada
class DoubleLinkedListIterator:
    def __init__(self, list_head):
        self._actual = list_head

    def __iter__(self):
        return self
    def __next__(self):
        if self._actual is None:
            raise StopIteration
        else:
            item = self._actual._valor
            self._actual = self._actual._next
            return item

def main():
    lista1 = Lista()
    assert lista1.EsVacia(), "Error en funcion EsVacia"
    assert len(lista1) == 0, "Error en funcion __len__"

    try:
        lista1.Head()
    except AssertionError:
        pass

    try:
        lista1.Tail()
    except AssertionError:
        pass

    lista1.AgregarIzquierda(3)
    assert not lista1.EsVacia(), "Error en funcion EsVacia"
    assert len(lista1) == 1, "Error en funcion __len__"
    assert lista1.Head() == 3, "Error en funcion Head"
    assert lista1.Tail() == 3, "Error en funcion Tail"

    lista2 = Lista()
    lista2.AgregarDerecha(2)
    assert not lista2.EsVacia(), "Error en funcion EsVacia"
    assert len(lista2) == 1, "Error en funcion  __len__"
    assert lista2.Head() == 2, "Error en funcion Head"
    assert lista2.Tail() == 2, "Error en funcion Tail"

    lista3 = Lista(4)
    assert not lista3.EsVacia(), "Error en funcion EsVacia"
    assert len(lista3) == 1, "Error en funcion __len__"
    assert lista3.Head() == 4, "Error en funcion Head"
    assert lista3.Tail() == 4, "Error en funcion Tail"

    lista1.AgregarIzquierda(5)
    assert not lista1.EsVacia(), "Error en funcion EsVacia"
    assert len(lista1) == 2, "Error en funcion __len__"
    assert lista1.Head() == 5, "Error en funcion Head"
    assert lista1.Tail() == 3, "Error en funcion Tail"

    lista1.AgregarDerecha(7)
    assert not lista1.EsVacia(), "Error en funcion EsVacia"
    assert len(lista1) == 3, "Error en funcion __len__"
    assert lista1.Head() == 5, "Error en funcion Head"
    assert lista1.Tail() == 7, "Error en funcion Tail"

    lista1.EliminarIzquierda()
    assert not lista1.EsVacia(), "Error en funcion EsVacia"
    assert len(lista1) == 2, "Error en funcion __len__"
    assert lista1.Head() == 3, "Error en funcion Head"
    assert lista1.Tail() == 7, "Error en funcion Tail"

    lista1.EliminarDerecha()
    assert not lista1.EsVacia(), "Error en funcion EsVacia"
    assert len(lista1) == 1, "Error en funcion __len__"
    assert lista1.Head() == 3, "Error en funcion Head"
    assert lista1.Tail() == 3, "Error en funcion Tail"

    lista1.EliminarIzquierda()
    assert lista1.EsVacia(), "Error en funcion EsVacia"
    assert len(lista1) == 0, "Error en funcion __len__"

    lista2.EliminarDerecha()
    assert lista2.EsVacia(), "Error en funcion EsVacia"
    assert len(lista2) == 0, "Error en funcion __len__"

    lista1.AgregarDerecha(7)
    lista1.AgregarIzquierda(3)
    lista1.AgregarIzquierda(5)
    lista3.AgregarDerecha(6)
    lista4 = lista1.Concatenar(lista3)
    assert not lista4.EsVacia(), "Error en funcion EsVacia"
    assert len(lista4) == 5, "Error en funcion __len__"
    assert lista4.Head() == 5, "Error en funcion Head"
    assert lista4.Tail() == 6, "Error en funcion Tail"

    lista4.Recorrer()
    lista4.RecorrerReverso()

    assert 7 in lista4, "Error en __contains__"
    assert not 9 in lista4, "Error en __contains__"

    for item in lista4:
        print(item, end = " ")
    print()

    print("Todos los casos estan OK.")

if __name__ == "__main__":
    main()
