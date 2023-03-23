/*
 * Implementacion en C de la estructura lista doblemente enlazada
 */

typedef long Elemento;

typedef struct NOdo {
  Elemento valor;
  struct NOdo *prev;
  struct NOdo *next;
} Nodo;

typedef struct LIsta {
  long longitud;
  Nodo *head, *tail;
} Lista;

extern void ListaVacia(Lista*);
extern int EsListaVacia(Lista);
extern long Longitud(Lista);
extern Lista* Unitaria(Elemento);
extern Elemento Head(Lista);
extern Elemento Tail(Lista);
extern void AgregarIzquierda(Elemento, Lista*);
extern void AgregarDerecha(Elemento, Lista*);
extern void EliminarIzquierda(Lista*);
extern void EliminarDerecha(Lista*);
