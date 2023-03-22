# Implementacion de pila usando arreglos
from arreglo import Arreglo

class Pila():
    def __init__(self, N = 10000):
        self._contenido = Arreglo(N)
        self._cantidad = 0

    def EsVacia(self):
        return self._cantidad == 0

    def Push(self, elemento):
        assert self._cantidad < len(self._contenido), "Espacio insuficiente."
        self._contenido[self._cantidad] = elemento
        self._cantidad += 1

    def Pop(self):
        assert not self.EsVacia(), "Pila vacia."
        self._cantidad -= 1

    def Top(self):
        assert not self.EsVacia(), "Pila vacia."
        return self._contenido[self._cantidad - 1]

def main():
    p = Pila()
    assert p.EsVacia(), "Error en constructor."

    try:
        p.Pop()
    except AssertionError:
        pass

    try:
        p.Top()
    except AssertionError:
        pass

    p.Push('P')
    assert not p.EsVacia(), "Error en funcion Push."
    assert p.Top() == 'P', "Error en funcion Top."

    p.Push('U')
    p.Push('C')
    p.Push('P')
    p.Pop()
    assert p.Top() == 'C', "Error en funcion Pop."
    print("Todos los casos estan OK.")

if __name__ == "__main__":
    main()
