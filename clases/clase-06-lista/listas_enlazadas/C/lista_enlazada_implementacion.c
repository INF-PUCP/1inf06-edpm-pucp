#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "lista_enlazada.h"

MAX_N = 5;

int Preparar(Nodo* ptr, int n) {
  int pos = 0;
  while (pos < n) {
    ptr->valor = pos + 1;
    ptr->next = ptr + 1;
    printf("ptr apunta a %p, valor = %d, next = %p.\n",
        ptr, ptr->valor, ptr->next);
    pos++;
    ptr++;
  }
  (ptr - 1)->next = NULL;
  printf("Ultimo nodo apunta a %p, valor = %d, next = %p.\n",
      ptr - 1, (ptr - 1)->valor, (ptr - 1)->next);
  return pos;
}

void Imprimir(Nodo* ptr) {
  int primera = 1;
  while (ptr != NULL) {
    if (!primera) printf(" -> ");
    printf("%d", ptr->valor);
    primera = 0;
    ptr = ptr->next;;
  }
  printf("\n");
}

Nodo* CopiarRecursivo(Nodo* ptr) {
  Nodo* nuevo;
  Nodo* siguiente;
  if (ptr == (Nodo*)(NULL)) {
    return NULL;
  } else {
    siguiente = CopiarRecursivo(ptr->next);
    nuevo = (Nodo*) malloc(sizeof(Nodo));
    nuevo->valor = ptr->valor;
    nuevo->next = siguiente;
    printf("nuevo apunta a %p, valor = %d, next = %p.\n",
        nuevo, nuevo->valor, nuevo->next);
    return nuevo;
  }
}

Nodo* CopiarIterativo(Nodo* ptr) {
  Nodo *nuevo, *r, *s, *t;
  if (ptr == NULL) {
    return NULL;
  } else {
    r = ptr;
    nuevo = (Nodo*) malloc(sizeof(Nodo));
    nuevo->valor = r->valor;
    printf("nuevo apunta a %p, valor = %d.\n", nuevo, nuevo->valor);
    s = nuevo;
    while (r->next != NULL) {
      r = r->next;
      t = (Nodo*) malloc(sizeof(Nodo));
      t->valor = r->valor;
      s->next = t;
      printf("next = %p.\n", s->next);
      printf("t apunta a %p, valor = %d.\n", t, t->valor);
      s = t;
    }
    s->next = NULL;
    printf("next = %p.\n", s->next);
    return nuevo;
  }
}

Nodo* Anular(Nodo* ptr) {
  Nodo* actual;
  while (ptr != NULL) {
    actual = ptr;
    ptr = ptr->next;
    free(actual);
  }
  return NULL;
}
