def profundidad(self):
    if self.es_pila_vacia_():
        return 0
    else:
        elemento = self.cima()
        self.desapilar()
        respuesta = 1 + self.profundidad()
        self.apilar(elemento)
        return respuesta
