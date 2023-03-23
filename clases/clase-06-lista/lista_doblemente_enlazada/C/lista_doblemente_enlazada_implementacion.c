#include <stdio.h>
#include <stdlib.h>
#include "lista_doblemente_enlazada.h"

void ListaVacia(Lista* lista) {
  lista->longitud = 0;
  lista->head = lista->tail = NULL;
}

int EsListaVacia(Lista lista) {
  return (lista.head == NULL);
}

long Longitud(Lista lista) {
  return lista.longitud;
}

Lista* Unitaria(Elemento elemento) {
  Lista* lista;
  Nodo* actual;
  lista = (Lista*) malloc(sizeof(Lista));
  if (lista == NULL) {
    printf("Error of Lista memory allocation.\n");
    exit(1);
  }
  actual = (Nodo*) malloc(sizeof(Nodo));
  if (actual == NULL) {
    printf("Error of Nodo memory allocation.\n");
    exit(2);
  }
  actual->valor = elemento;
  actual->prev = actual->next = NULL;
  lista->head = lista->tail = actual;
  lista->longitud = 1;
  return lista;
}

Elemento Head(Lista lista) {
  if (lista.head == NULL) {
    printf("Error: Lista vacia.\n");
    exit(3);
  }
  return lista.head->valor;
}

Elemento Tail(Lista lista) {
  if (lista.tail == NULL) {
    printf("Error: Lista vacia.\n");
    exit(4);
  }
  return lista.tail->valor;
}

void AgregarIzquierda(Elemento elemento, Lista* lista) {
  Nodo* nuevo;
  nuevo = (Nodo*) malloc(sizeof(Nodo));
  if (nuevo == NULL) {
    printf("Error of Nodo memory allocation.\n");
    exit(5);
  }
  nuevo->valor = elemento;
  nuevo->prev = NULL;
  if (lista->head == NULL) {
    nuevo->next = NULL;
    lista->tail = nuevo;
  } else {
    nuevo->next = lista->head;
    lista->head->prev = nuevo;
  }
  lista->head = nuevo;
  lista->longitud++;
}

void AgregarDerecha(Elemento elemento, Lista* lista) {
  Nodo* nuevo;
  nuevo = (Nodo*) malloc(sizeof(Nodo));
  if (nuevo == NULL) {
    printf("Error of Nodo memory allocation.\n");
    exit(6);
  }
  nuevo->valor = elemento;
  nuevo->next = NULL;
  if (lista->tail == NULL) {
    nuevo->prev = NULL;
    lista->head = nuevo;
  } else {
    nuevo->prev = lista->tail;
    lista->tail->next = nuevo;
  }
  lista->tail = nuevo;
  lista->longitud++;
}

void EliminarIzquierda(Lista* lista) {
  Nodo* actual;
  if (lista->head == NULL) {
    printf("Error: Lista vacia.\n");
    exit(7);
  }
  actual = lista->head;
  lista->head = actual->next;
  if (lista->head == NULL) lista->tail = NULL;
  else lista->head->prev = NULL;
  lista->longitud--;
  free(actual);
}

void EliminarDerecha(Lista* lista) {
  Nodo* actual;
  if (lista->tail == NULL) {
    printf("Error: Lista vacia.\n");
    exit(8);
  }
  actual = lista->tail;
  lista->tail = actual->prev;
  if (lista->tail == NULL) lista->head = NULL;
  else lista->tail->next = NULL;
  lista->longitud--;
  free(actual);
}
