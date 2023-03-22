#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "ejercicio_2_1_a.h"

Conjunto ConjuntoVacio(void) {
  Elemento* ptr;
  Conjunto resultado;
  ptr = (Elemento*) calloc(MAX_N, sizeof(Elemento));
  if (ptr == NULL) {
    printf("Error of memory allocation.\n");
    exit(1);
  }
  assert(*ptr == 0 && *(ptr + MAX_N - 1) == 0);  // calloc limpia con 0 la memoria
  resultado.contenido = ptr;
  resultado.cantidad = 0;
  return resultado;
}

int EsConjuntoVacio(Conjunto x) {
  return (x.cantidad == 0);
}

Conjunto ConjuntoUnitario(Elemento elemento) {
  Elemento* ptr;
  Conjunto resultado;
  ptr = (Elemento*) calloc(MAX_N, sizeof(Elemento));
  if (ptr == NULL) {
    printf("Error of memory allocation.\n");
    exit(1);
  }
  assert(*ptr == 0 && *(ptr + MAX_N - 1) == 0);
  *ptr = elemento;
  resultado.contenido = ptr;
  resultado.cantidad = 1;
  return resultado;
}

int Pertenece(Elemento elemento, Conjunto conjunto) {
  int encontrado = 0;
  int pos = 0;
  while (pos < conjunto.cantidad) {
    if (elemento == *(conjunto.contenido + pos)) {
      encontrado = 1;
      break;
    }
    pos++;
  }
  return encontrado;
}

void Agregar(Elemento elemento, Conjunto* conjunto) {
  if (conjunto->cantidad == MAX_N - 1) {
    printf("Espacio insuficiente.\n");
    exit(3);
  }
  *(conjunto->contenido + conjunto->cantidad) = elemento;
  (conjunto->cantidad)++;
}

void Quitar(Elemento elemento, Conjunto* conjunto) {
  int pos = 0;
  while (pos < (conjunto->cantidad)) {
    if (*(conjunto->contenido + pos) == elemento) {
      // Si es que aparece, el ultimo elemento lo coloco en su posicion
      *(conjunto->contenido + pos) = *(conjunto->contenido + conjunto->cantidad - 1);
      (conjunto->cantidad)--;
    } else {
      pos++;
    }
  }
}

Conjunto Union(Conjunto c1, Conjunto c2) {
  Conjunto c = ConjuntoVacio();
  for (int i = 0; i < c1.cantidad; i++) Agregar(*(c1.contenido + i), &c);
  for (int i = 0; i < c2.cantidad; i++) Agregar(*(c2.contenido + i), &c);
  return c;
}

Conjunto Interseccion(Conjunto c1, Conjunto c2) {
  Conjunto c = ConjuntoVacio();
  for (int i = 0; i < c1.cantidad; i++) {
    if (Pertenece(*(c1.contenido + i), c2))
      Agregar(*(c1.contenido + i), &c);
  }
  return c;
}

Conjunto Diferencia(Conjunto c1, Conjunto c2) {
  Conjunto c = ConjuntoVacio();
  for (int i = 0; i < c1.cantidad; i++) {
    if (!Pertenece(*(c1.contenido + i), c2))
      Agregar(*(c1.contenido + i), &c);
  }
  return c;
}

int Cardinalidad(Conjunto* antiguo) {
  Conjunto nuevo = ConjuntoVacio();
  for (int i = 0; i < antiguo->cantidad; i++) {
    if (!Pertenece(*(antiguo->contenido + i), nuevo))
      Agregar(*(antiguo->contenido + i), &nuevo);
  }
  free(antiguo->contenido);  // Liberamos la memoria del conjunto antiguo
  *antiguo = nuevo;
  return antiguo->cantidad;
}
