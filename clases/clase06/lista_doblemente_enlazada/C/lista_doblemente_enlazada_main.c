#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "lista_doblemente_enlazada.h"

int main(void) {
  Lista lista;
  ListaVacia(&lista);
  assert(lista.longitud == 0 && lista.head == NULL && lista.tail == NULL);

  assert(EsListaVacia(lista));
  assert(Longitud(lista) == 0);

  Lista* aux;
  aux = Unitaria(69);
  assert(!EsListaVacia(*aux));
  assert(Longitud(*aux) == 1);
  assert(Head(*aux) == 69);
  assert(Tail(*aux) == 69);

  AgregarIzquierda(2, &lista);
  assert(!EsListaVacia(lista));
  assert(Longitud(lista) == 1);
  assert(Head(lista) == 2);
  assert(Tail(lista) == 2);

  AgregarIzquierda(1, &lista);
  assert(!EsListaVacia(lista));
  assert(Longitud(lista) == 2);
  assert(Head(lista) == 1);
  assert(Tail(lista) == 2);

  AgregarDerecha(3, &lista);
  assert(Longitud(lista) == 3);
  assert(Head(lista) == 1);
  assert(Tail(lista) == 3);

  AgregarIzquierda(16, aux);
  assert(!EsListaVacia(*aux));
  assert(Longitud(*aux) == 2);
  assert(Head(*aux) == 16);
  assert(Tail(*aux) == 69);

  AgregarDerecha(18, aux);
  assert(Longitud(*aux) == 3);
  assert(Head(*aux) == 16);
  assert(Tail(*aux) == 18);
  printf("Todos los casos estan OK.\n");
  exit(EXIT_SUCCESS);
  return 0;
}
