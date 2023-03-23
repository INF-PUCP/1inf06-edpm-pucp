#include <stdio.h>
#include <stdlib.h>
#include "arbol_binario.h"

Arbol ArbolVacio(void) {
  return ((Arbol) NULL);
}

Arbol Plantar(Arbol izq, Elemento e, Arbol der) {
  Arbol nuevo = (Arbol) malloc(sizeof(Nodo));
  if (nuevo == NULL) {
    printf("Error of memory allocation\n");
    exit(1);
  }
  nuevo->valor = e;
  nuevo->izquierda = izq;
  nuevo->derecha = der;
  return nuevo;
}

Arbol Izquierda(Arbol a) {
  if (a == NULL) {
    printf("Error: Arbol vacio\n");
    exit(2);
  }
  return a->izquierda;
}

Arbol Derecha(Arbol a) {
  if (a == NULL) {
    printf("Error: Arbol vacio\n");
    exit(3);
  }
  return a->derecha;
}

Elemento Raiz(Arbol a) {
  if (a == NULL) {
    printf("Error: Arbol vacio\n");
    exit(4);
  }
  return a->valor;
}

int Vacio(Arbol a) {
  return (a == NULL);
}
