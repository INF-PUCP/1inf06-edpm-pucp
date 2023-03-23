/*
 * Definicinoes de los tipos de datos y prototipos de las funciones
 * que trabajan con las listas enlazadas
 */

int MAX_N;

typedef long Elemento;

typedef struct NOdo {
  Elemento valor;
  struct NOdo* next;
} Nodo;

extern int Preparar(Nodo*, int);
extern void Imprimir(Nodo*);
extern Nodo* CopiarRecursivo(Nodo*);
extern Nodo* CopiarIterativo(Nodo*);
extern Nodo* Anular(Nodo*);
