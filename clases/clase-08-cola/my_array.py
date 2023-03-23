import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, "Tamaño del arreglo tiene que ser positivo"
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Fuera de límites del arreglo"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Fuera de límites del arreglo"
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self, cur):
        self._array_ref = cur
        self._cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur < len(self._array_ref):
            tmp = self._array_ref[self._cur]
            self._cur += 1
            return tmp
        else:
            raise StopIteration
