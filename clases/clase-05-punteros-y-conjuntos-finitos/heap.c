#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

void Heap1() {
  // Alocacion de una variable local que es un puntero local
  int* intPtr;
  
  // Alocacion a un bloque del heap y guarda su puntero en la variable local
  intPtr = malloc(sizeof(int));
  // Dereferencia el puntero para colocarle el valor 42
  *intPtr = 42;

  // Dealocacion del bloque del heap y haciendo invalido el puntero
  // No usar este puntero luego de que la direcci[on ha sido dealocada
  free(intPtr);
}

struct fraccion {
  int numerador;
  int denominador;
};

void HeapArray() {
  struct fraccion* fracciones;
  int i;
  // Alocamos el arreglo
  fracciones = malloc(sizeof(struct fraccion) * 100);

  // Lo usamos como arreglo
  for (int i = 0; i < 99; i++) {
    fracciones[i].numerador = 22;
    fracciones[i].denominador = 7;
  }

  // Dealocamos el arreglo
  free(fracciones);
}

/*
 * Dada una cadena en C, retorne una copia alocada en el heap de la cadena.
 * Alocar un bloque en el heap del tama~no apropieado,
 * copie la cadena en el bloque, y retorne el puntero a el bloque.
 * El invocador sera el nuevo responsable del bloque y de liberar su memoria
 */
char* CopiarCadena(const char* cadena) {
  char* copia;
  int longitud;
  longitud = strlen(cadena) + 1;  // +1 para tener al caracter '\0'
  copia = malloc(sizeof(char) * longitud);
  assert(copia != NULL);
  strcpy(copia, cadena);
  return copia;  // retorno el puntero al bloque
}

int main() {
  char* s = "Manuel";
  char* t = CopiarCadena(s);
  printf("Mi nombre es %s.\n", t);
  return 0;
}
