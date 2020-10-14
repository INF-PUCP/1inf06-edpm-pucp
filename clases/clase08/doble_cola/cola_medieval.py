from doble_cola import DobleCola

class ColaMedieval:
    def __init__(self):
        self._nobles = DobleCola()
        self._plebeyos = DobleCola()

    def __len__(self):
        return len(self._nobles) + len(self._plebeyos)

    def count(self, tag):
        if tag.lower() == "noble":
            return len(self._nobles)
        else:
            return len(self._plebeyos)

    def empty(self):
        return len(self) == 0

    def front(self):
        assert not self.empty(), "Cola medieval vacia"
        if not self._nobles.empty():
            return self._nobles.front()
        else:
            return self._plebeyos.front()

    def push(self, item, tag):
        if tag.lower() == "noble":
            self._nobles.push_back(item)
        else:
            self._plebeyos.push_back(item)

    def pop(self):
        assert not self.empty(), "Cola medieval vacia"
        if not self._nobles.empty():
            return self._nobles.pop_front()
        else:
            return self._plebeyos.pop_front()

def main():
    q = ColaMedieval()
    assert q.empty(), "Error en empty"

    try:
        q.pop()
    except AssertionError:
        pass

    q.push(4, "plebeyo")
    assert not q.empty(), "Error en empty"

    q.push(2, "plebeyo")
    assert q.pop() == 4, "Error en pop"
    assert q.pop() == 2, "Error en pop"
    assert q.empty(), "Error en empty"

    q.push(3, "noble")
    q.push(1, "noble")
    assert q.pop() == 3, "Error en pop"
    assert q.pop() == 1, "Error en pop"
    assert q.empty(), "Error en empty"

    q.push(8, "plebeyo")
    q.push(6, "plebeyo")
    q.push(7, "noble")
    q.push(5, "noble")
    q.push(10, "plebeyo")
    assert len(q) == 5, "Error en len"
    assert q.count("noble") == 2 and q.count("plebeyo") == 3, "Error en count"
    assert q.pop() == 7, "Error en pop"
    assert q.pop() == 5, "Error en pop"
    assert q.pop() == 8, "Error en pop"
    assert q.pop() == 6, "Error en pop"
    assert q.pop() == 10, "Error en pop"
    assert q.empty(), "Error en empty"

    print("Todos los casos estan OK")

if __name__ == "__main__":
    main()
