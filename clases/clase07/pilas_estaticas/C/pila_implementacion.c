#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "pila.h"

Pila PilaVacia(void) {
  Elemento* ptr;
  Pila pila;
  ptr = (Elemento*) calloc(N, sizeof(Elemento));
  pila.contenido = ptr;
  pila.cantidad = 0;
  return pila;
}

int EsVacia(Pila pila) {
  return (pila.cantidad == 0);
}

// Añado elemento a la pila
void Push(Elemento elemento, Pila* pila) {
  if (pila->cantidad == N) {
    printf("Espacio insuficiente.\n");
    exit(1);
  }
  *(pila->contenido + pila->cantidad) = elemento;
  (pila->cantidad)++;
}

// Desapilo ultimo elemento en la pila
void Pop(Pila* pila) {
  if (pila->cantidad == 0) {
    printf("Pila vacia.\n");
    exit(2);
  }
  (pila->cantidad)--;
}

// Retorno el ultimo elemento en la pila
Elemento Top(Pila pila) {
  if (pila.cantidad == 0) {
    printf("Pila vacia.\n");
    exit(3);
  }
  return *(pila.contenido + (pila.cantidad - 1));
}
