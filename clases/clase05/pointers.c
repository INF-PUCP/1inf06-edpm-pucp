#include <stdio.h>

int main() {
  int* ptr = NULL;  // ptr es un puntero a entero, se sugiere inicializarlo
  int a = 5;
  ptr = &a;  // asignamos la direccion de a a ptr
  *ptr = 8;  // desreferenciamos ptr

  int var1;
  char var2[10];
  printf("Direccion de var1: %x\n", &var1);
  printf("Direccion de var2: %x\n", &var2);

  int var = 20;
  int* ip;
  ip = &var;
  printf("Direccion de var: %x\n", &var);
  printf("Direccion guardada en ip: %x\n", ip);
  printf("Valor de la variable *ip: %d\n", *ip);

  ptr = NULL;
  printf("El valor de ptr es %x\n", ptr);
  if (ptr) {
    printf("ptr no es nulo\n");
  } else {
    printf("ptr es nulo\n");
  }

  int x = 1;
  int y = 2;
  int z[10];
  int* id;
  printf("\nx: address = %p, size = %d, value = %d\n",
      &x, sizeof(x), x);
  printf("y: address = %p, size = %d, value = %d\n",
      &y, sizeof(y), y);
  printf("z: address = %p, size = %d, z[0] = %d\n",
      z, sizeof(z), z[0]);
  printf("id: address = %p, size = %d, value = %p\n",
      &id, sizeof(id), id);

  id = &x;  // id ahora a punta a x
  printf("\nid: address = %p, size = %d, value = %p\n",
      &id, sizeof(id), id);
  y = *id;  // y ahora vale 1
  printf("y: address = %p, size = %d, value = %d\n",
      &y, sizeof(y), y);
  id++;  // id se incrementa en sizeof(int)
  printf("id: address = %p, size = %d, value = %p\n",
      &id, sizeof(id), id);
  id--;
  printf("id: address = %p, size = %d, value = %p\n",
      &id, sizeof(id), id);

  *id = 0;  // x ahora vale 0
  id = &z[0];  // id apunta a z[0]
  printf("\nid: address = %p, size = %d, value = %p\n",
      &id, sizeof(id), id);
  id = z;  // id sigue a puntando a z[0]
  printf("id: address = %p, size = %d, value = %p\n",
      &id, sizeof(id), id);
  *id = x;  // z[0] ahora vale 0
  printf("z[0]: address = %p, size = %d, value = %d\n",
      &z[0], sizeof(z[0]), z[0]);
  *id += 2;  // z[0] ahora vale 2
  printf("z[0]: address = %p, size = %d, value = %d\n",
      &z[0], sizeof(z[0]), z[0]);
  printf("z[1]: address = %p, size = %d, value = %d\n",
      &z[1], sizeof(z[1]), z[1]);

  *(id + 1) = *id * 2;  // ip apunto a z[0], z[1] ahora vale 4
  printf("z[0]: address = %p, size = %d, value = %d\n",
      &z[0], sizeof(z[0]), z[0]);
  printf("z[1]: address = %p, size = %d, value = %d\n",
      &z[1], sizeof(z[1]), z[1]);
  printf("z[2]: address = %p, size = %d, value = %d\n",
      &z[2], sizeof(z[2]), z[2]);
  return 0;
}
