class DobleCola:
    class Nodo:
        def __init__(self, item):
            self._item = item
            self._prev = None
            self._next = None

    def __init__(self):
        self._front = None
        self._back = None
        self._cnt = 0

    def empty(self):
        return self._front is None

    def front(self):
        assert not self.empty(), "Doble cola vacia"
        return self._front._item

    def back(self):
        assert not self.empty(), "Doble cola vacia"
        return self._back._item
    
    def __len__(self):
        return self._cnt

    def push_front(self, item):
        cur = self.Nodo(item)
        if self.empty():
            self._front = cur
            self._back = cur
        else:
            cur._next = self._front
            self._front._prev = cur
            self._front = cur
        self._cnt += 1
    
    def push_back(self, item):
        cur = self.Nodo(item)
        if self.empty():
            self._front = cur
            self._back = cur
        else:
            cur._prev = self._back
            self._back._next = cur
            self._back = cur
        self._cnt += 1

    def pop_front(self):
        assert not self.empty(), "Doble cola vacia"
        ret = self._front._item
        if len(self) == 1:
            self._front = None
            self._back = None
        else:
            self._front = self._front._next
            self._front._prev = None
        self._cnt -= 1
        return ret

    def pop_back(self):
        assert not self.empty(), "Doble cola vacia"
        ret = self._back._item
        if len(self) == 1:
            self._front = None
            self._back = None
        else:
            self._back = self._back._prev
            self._back._next = None
        self._cnt -= 1
        return ret

def main():
    q = DobleCola()
    assert q.empty(), "Error en empty"

    try:
        q.pop_front()
    except AssertionError:
        pass

    try:
        q.pop_back()
    except AssertionError:
        pass

    q.push_back(3)
    assert not q.empty(), "Error en push_back"
    assert q.front() == 3, "Error en front"
    assert q.back() == 3, "Error en back"

    q.pop_back()
    assert q.empty(), "Error en pop_back"

    try:
        q.front()
    except AssertionError:
        pass

    try:
        q.back()
    except AssertionError:
        pass

    q.push_front(1)
    q.pop_front()
    assert q.empty(), "Error en pop_front"

    try:
        q.front()
    except AssertionError:
        pass

    try:
        q.back()
    except AssertionError:
        pass

    q.push_front(1)
    assert not q.empty(), "Error en push_front"
    assert q.front() == 1, "Error en front"
    assert q.back() == 1, "Error en back"

    q.pop_back()
    assert q.empty(), "Erroren pop_back"

    try:
        q.front()
    except AssertionError:
        pass

    try:
        q.back()
    except AssertionError:
        pass

    q.push_back(3)
    q.push_back(4)
    q.push_front(2)
    q.push_front(1)

    assert q.front() == 1, "Error en front"
    assert q.back() == 4, "Error en back"
    assert not q.empty(), "Error en empty"
    q.pop_front()
    q.pop_back()
    assert q.front() == 2, "Error en front"
    assert q.back() == 3, "Error en back"

    print("Todos los casos estan OK")

if __name__ == "__main__":
    main()
