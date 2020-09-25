# Implementacion del TAD arreglo usando capabilidades de ctypes module
import ctypes

class Arreglo:
    def __init__(self, size):
        assert size > 0, "El tamaño del arreglo debe ser positivo."
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Indice fuera de limites."
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Indice fuera de limites."
        self._elements[index] = value

    def clear(self, value):
        for ind in range(len(self)):
            self._elements[ind] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self, arr):
        self._arr = arr
        self._cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur < len(self._arr):
            entry = self._arr[self._cur]
            self._cur += 1
            return entry
        else:
            raise StopIteration
