/*
 * Implementacion del TAD de los conjuntos finitos utilizando como
 * representacion del tipo Conjunto como vectores de Elementos
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "ejercicio_2_1_a.h"

// (tamanio del arreglo, arreglo)
int main(int argc, char* argv[]) {
  // Si al invocar el programa no me dieron el tamanio, uso 10^4 por defecto
  if (argc == 1) {
    MAX_N = 10000;
  } else {
    MAX_N = atoi(argv[1]);
  }
  printf("El conjunto puede tener hasta %d elementos.\n", MAX_N);

  Conjunto conjunto1 = ConjuntoVacio();
  assert(EsConjuntoVacio(conjunto1));

  Conjunto conjunto2 = ConjuntoUnitario(69);
  assert(!EsConjuntoVacio(conjunto2));
  assert(*(conjunto2.contenido) == 69);
  assert(Pertenece(69, conjunto2));
  //assert(!Pertenece(69, conjunto2));
  
  Agregar(6, &conjunto1);
  Agregar(6, &conjunto1);
  Quitar(6, &conjunto1);
  assert(EsConjuntoVacio(conjunto1));

  Agregar(6, &conjunto2);
  Agregar(69, &conjunto2);
  Quitar(69, &conjunto2);
  assert(Pertenece(6, conjunto2));
  assert(!Pertenece(69, conjunto2));

  Conjunto conjunto3 = Diferencia(conjunto2, conjunto1);
  assert(Pertenece(6, conjunto3));
  free(conjunto3.contenido);

  Agregar(69, &conjunto1);
  conjunto3 = Union(conjunto1, conjunto2);
  assert(Pertenece(6, conjunto3));
  assert(Pertenece(69, conjunto3));
  free(conjunto3.contenido);

  Agregar(6, &conjunto1);
  conjunto3 = Interseccion(conjunto1, conjunto2);
  assert(Pertenece(6, conjunto3));
  assert(!Pertenece(69, conjunto3));
  free(conjunto3.contenido);

  Agregar(69, &conjunto1);
  assert(Cardinalidad(&conjunto1) == 2);
  assert(Pertenece(6, conjunto1));
  assert(Pertenece(69, conjunto1));
  assert(Cardinalidad(&conjunto2) == 1);

  free(conjunto1.contenido);
  free(conjunto2.contenido);
  printf("Todos los casos estan OK.\n");
  return 0;
}
