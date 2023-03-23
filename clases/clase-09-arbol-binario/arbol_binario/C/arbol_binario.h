typedef long Elemento;

typedef struct Nodo {
  Elemento valor;
  struct Nodo* izquierda;
  struct Nodo* derecha;
} Nodo;

typedef Nodo* Arbol;

extern Arbol ArbolVacio(void);
extern Arbol Plantar(Arbol, Elemento, Arbol);
extern Arbol Izquierda(Arbol);
extern Arbol Derecha(Arbol);
extern Elemento Raiz(Arbol);
extern int Vacio(Arbol);
