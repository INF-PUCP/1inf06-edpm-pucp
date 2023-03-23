#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "pila.h"

int main(int argc, char* argv[]) {
  Pila p;
  Elemento e;

  if (argc == 1) {
    N = 10000;
  } else {
    N = atoi(argv[1]);
  }
  printf("La pila puede tener hasta %d elementos.\n", N);

  p = PilaVacia();
  assert(EsVacia(p));
  e.valor = 5;
  Push(e, &p);
  e.valor = 8;
  Push(e, &p);
  e.valor = 0;
  Push(e, &p);
  e.valor = 3;
  Push(e, &p);

  assert(Top(p).valor == 3);
  Pop(&p);
  assert(Top(p).valor == 0);
  Pop(&p);
  assert(Top(p).valor == 8);
  Pop(&p);
  assert(Top(p).valor == 5);
  Pop(&p);
  assert(EsVacia(p));

  free(p.contenido);
  printf("Todos los casos estan OK.\n"); 
  exit(EXIT_SUCCESS);
  return 0;
}
