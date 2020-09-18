/*
 * Definiciones de los tipos de datos y prototipos de las funciones
 * que trabajan con los conjuntos
 */

int MAX_N;

typedef long Elemento;

typedef struct COnjunto {
  Elemento* contenido;
  int cantidad;
} Conjunto;

extern Conjunto ConjuntoVacio(void);
extern int EsConjuntoVacio(Conjunto);
extern Conjunto ConjuntoUnitario(Elemento);
extern int Pertenece(Elemento, Conjunto);
extern void Agregar(Elemento, Conjunto*);
extern void Quitar(Elemento, Conjunto*);
extern Conjunto Union(Conjunto, Conjunto);
extern Conjunto Interseccion(Conjunto, Conjunto);
extern Conjunto Diferencia(Conjunto, Conjunto);
extern int Cardinalidad(Conjunto*);
