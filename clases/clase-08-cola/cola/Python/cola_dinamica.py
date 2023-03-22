class Cola:
    class Nodo:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._cnt = 0

    def empty(self):
        return self._head is None

    def __len__(self):
        return self._cnt

    def push(self, item):
        cur = self.Nodo(item)
        if self.empty():
            self._head = cur
        else:
            self._tail.next = cur
        self._tail = cur
        self._cnt += 1

    def pop(self):
        assert not self.empty(), "Cola vacia"
        ret = self._head.item
        if self._cnt == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
        self._cnt -= 1
        return ret

def main():
    q = Cola()
    assert q.empty(), "Error en empty"
    try:
        q.pop()
    except AssertionError:
        pass

    q.push(1)
    assert not q.empty(), "Error en empty"

    q.push(2)
    q.push(2)
    assert len(q) == 3, "Error en len"

    q.push(3)
    assert q.pop() == 1, "Error en pop"
    assert len(q) == 3, "Error en len"

    print("Todos los casos estan OK")

if __name__ == "__main__":
    main()
