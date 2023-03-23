#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "arbol_binario.h"

int main(void) {
  Elemento e;
  Arbol a, b, c, d, f, g;
  a = ArbolVacio();
  assert(Vacio(a));
  b = ArbolVacio();
  c = ArbolVacio();

  a = Plantar(b, 1, c);
  assert(!Vacio(a));
  assert(Vacio(Izquierda(a)));
  assert(Vacio(Derecha(a)));
  assert(Raiz(a) == 1);

  d = Plantar(b, 2, c);
  f = Plantar(b, 3, c);
  g = Plantar(d, 4, f);

  assert(!Vacio(g));
  assert(Raiz(g) == 4);
  assert(!Vacio(Izquierda(g)));
  assert(Raiz(Izquierda(g)) == 2);
  assert(!Vacio(Derecha(g)));
  assert(Raiz(Derecha(g)) == 3);

  free(a);
  free(d);
  free(f);
  free(g);

  printf("Todos los casos estan OK\n");
  return 0;
}
