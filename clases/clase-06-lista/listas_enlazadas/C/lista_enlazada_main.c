#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "lista_enlazada.h"

int main() {
  Nodo aux[512];
  Nodo* ptr;
  printf("La direccion del vector aux es %p.\n", aux);
  printf("Preparando los nodos en el vector aux ...\n");
  Preparar(aux, MAX_N);

  printf("\nListado de los nodos en el vector aux ...\n");
  Imprimir(aux);

  printf("\nCopiando los nodos a la lista enlazada ptr ...\n");
  ptr = CopiarRecursivo(aux);
  printf("ptr apunta a %p.\n", ptr);

  printf("\nListado de los nodos en el la lista enlazada ptr ...\n");
  Imprimir(ptr);

  printf("\nAnulando la lista ptr ...\n");
  ptr = Anular(ptr);
  printf("ptr apunta a %p.\n", ptr);

  printf("\nCopiando iterativamente aux a ptr ...\n");
  ptr = CopiarIterativo(aux);
  printf("ptr apunta a %p.\n", ptr);

  printf("\nListado de los nodos en la lista enlazada ptr ...\n");
  Imprimir(ptr);

  printf("\nAnulando al estructura ptr ...\n");
  ptr = Anular(ptr);
  printf("ptr apunta a %p.\n", ptr);
  return 0;
}
