int N;

typedef struct ELemento {
  long valor;
  unsigned int activo;
  long codigo;
  char nombre[5][20];
} Elemento;

typedef struct PIla {
  Elemento* contenido;
  unsigned long cantidad;
} Pila;

extern Pila PilaVacia(void);
extern int EsVacia(Pila);
extern void Push(Elemento, Pila*);
extern void Pop(Pila*);
extern Elemento Top(Pila);
