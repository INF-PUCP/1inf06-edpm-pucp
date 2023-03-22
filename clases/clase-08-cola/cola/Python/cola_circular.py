from my_array import Array

class Cola:
    def __init__(self, max_size=100):
        self._front = 0
        self._back = 0
        self._cnt = 0
        self._arr = Array(max_size)

    def empty(self):
        return self._cnt == 0

    def full(self):
        return self._cnt == len(self._arr)

    def __len__(self):
        return self._cnt

    def push(self, item):
        assert not self.full(), "Cola llena"
        if not self.empty():
            self._back = (self._back + 1) % len(self._arr)
        self._arr[self._back] = item
        self._cnt += 1

    def pop(self):
        assert not self.empty(), "Cola vacia"
        retirar = self._arr[self._front]
        if (len(self) > 1):
            self._front = (self._front + 1) % len(self._arr)
        self._cnt -= 1
        return retirar

def main():
    q = Cola(3)
    assert q.empty(), "Error en empty"
    assert not q.full(), "Error en full"

    try:
        q.pop()
    except AssertionError:
        pass

    q.push(1)
    assert not q.empty(), "Error en empty"

    q.push(2)
    q.push(2)
    assert len(q) == 3, "Error en len"
    assert q.full(), "Error en full"

    try:
        q.push(3)
    except AssertionError:
        pass

    assert q.pop() == 1, "Error en pop"
    q.push(4)
    assert q.full(), "Error en full"

    print("Todos los casos estan OK")

if __name__ == "__main__":
    main()
