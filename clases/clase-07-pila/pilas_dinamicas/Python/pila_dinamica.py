class Pila:
    class Nodo:
        def __init__(self, value=0, link=None):
            self.value = value
            self.next = link

    def __init__(self):
        self._top = None
        self._size = 0

    def empty(self):
        return self._top is None

    def __len__(self):
        return self._size

    def top(self):
        assert not self.empty(), "Pila vacia"
        return self._top.value

    def pop(self):
        assert not self.empty(), "Pila vacia"
        retirar = self._top
        self._top = self._top.next
        self._size -= 1
        return retirar.value

    def push(self, value):
        self._top = self.Nodo(value, self._top)
        self._size += 1

def main():
    p = Pila()
    assert p.empty(), "Error en empty"
    assert len(p) == 0, "Error en len"
    try:
        p.top()
    except AssertionError:
        pass

    try:
        p.pop()
    except AssertionError:
        pass

    p.push('M')
    assert not p.empty(), "Error en empty"
    assert len(p) == 1, "Error en len"
    assert p.top() == 'M', "Error en top"

    p.pop()
    assert p.empty(), "Error en empty"
    assert len(p) == 0, "Error en len"

    for c in "MANUEL":
        p.push(c)

    p.pop()
    assert len(p) == 5, "Error en len"
    assert p.top() == 'E', "Error en top"

    print("Todos los casos estan OK")

if __name__ == "__main__":
    main()
