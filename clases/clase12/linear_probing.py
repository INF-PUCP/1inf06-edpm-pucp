# Hashing with Linear Probing
DELTA = 31415926535897932

class HashTable:
    # Inicializamos un arreglo con tamano sz
    def __init__(self, sz = 10007):
        self._array = []
        self._size = sz
        for i in range(sz):
            self._array.append(None)

    # Funcion hash que utilizare
    def my_hash(self, item):
        return item % self._size

    # Anado item a la tabla
    def push(self, item):
        pos = self.my_hash(item)
        if (self._array[pos] is None):
            self._array[pos] = item
        else:
            for dist in range(self._size):
                to = (pos + dist) % self._size
                if (self._array[to] is None or self._array[to] == DELTA):
                    self._array[to] = item
                    return
            assert True, "Tabla llena"

    # Consulto si item pertenece a la tabla
    def find(self, item):
        pos = self.my_hash(item)
        for dist in range(self._size):
            to = (pos + dist) % self._size
            if (self._array[to] is None):
                return False
            if (self._array[to] == item):
                return True
        return False

    # Elimino item de la tabla
    def pop(self, item):
        assert self.find(item), "Item no pertenece a la tabla"
        pos = self.my_hash(item)
        for dist in range(self._size):
            to = (pos + dist) % self._size
            if (self._array[to] == item):
                self._array[to] = DELTA
                return

def main():
    ht = HashTable(7)
    ht.push(64)
    ht.push(52)
    ht.push(14)
    ht.push(31)
    ht.push(22)
    ht.push(18)
    ht.push(49)

    assert ht.find(64), "Error en find"
    assert ht.find(52), "Error en find"
    assert not ht.find(53), "Error en find"
    assert ht.find(14), "Error en find"
    assert not ht.find(100), "Error en find"
    assert ht.find(31), "Error en find"
    assert ht.find(22), "Error en find"
    assert ht.find(18), "Error en find"
    assert ht.find(49), "Error en find"
    assert not ht.find(55), "Error en find"

    ht.pop(18)
    assert not ht.find(18)

    print("Todos los casos estan OK")

if __name__ == "__main__":
    main()
