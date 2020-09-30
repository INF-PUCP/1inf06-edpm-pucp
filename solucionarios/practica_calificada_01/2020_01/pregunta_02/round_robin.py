class _QueueNode:
    def __init__(self, id, time = 0):
        self.id = id
        self.time = time
        self.next = None
class CQueue:
    # Creates an empty queue.
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0
    # Returns True if the queue is empty or False otherwise.
    def isEmpty(self):
        return self._qhead is None
    # Returns the number of items in the queue.
    def __len__(self):
        return self._count
    # Adds the given item to the queue.
    def enqueue(self, id, time):
        node = _QueueNode(id, time)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node
        node.next = self._qhead
        self._qtail = node
        self._count += 1
    # Removes and returns the first item in the queue.
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.id
    
    def roundrobin(self, q):
        nodo = self._qhead
        count = 0
        print("Estado inicial con turno (q) igual a: {}". format(q))
        print()
        while count < self._count:
            print((nodo.id, nodo.time), end = '')
            count += 1
            nodo = nodo.next
        print(); print()
        print("Procesando...")
        while True:
            # Modifico la cola
            count = 0
            nodo = self._qhead
            while count < self._count:
                nodo.time -= q
                nodo.time = max(0, nodo.time)
                print((nodo.id, nodo.time), end = '')
                count += 1
                nodo = nodo.next
            print()
            # Chequeo que no hayamos acabado
            terminado = True
            count = 0
            nodo = self._qhead
            while count < self._count:
                if nodo.time != 0:
                    terminado = False
                    break
                count += 1
                nodo = nodo.next
            if terminado:
                break

cq = CQueue()
cq.enqueue(1, 3)
cq.enqueue(2, 6)
cq.enqueue(3, 4)
cq.enqueue(4, 5)
cq.enqueue(5, 2)
cq.roundrobin(2)
