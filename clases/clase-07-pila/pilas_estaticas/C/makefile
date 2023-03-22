all: pila

pila:  pila_main.o pila_implementacion.o
	gcc -o pila pila_main.o pila_implementacion.o

pila_main.o: pila_main.c pila.h
	gcc -c pila_main.c

pila_implementacion.o: pila_implementacion.c pila.h
	gcc -c pila_implementacion.c

clean:
	-rm pila_main.o pila_implementacion.o
