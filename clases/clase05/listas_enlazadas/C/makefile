all: lista_enlazada

lista_enlazada: lista_enlazada_main.o lista_enlazada_implementacion.o
	gcc -o lista_enlazada lista_enlazada_main.o lista_enlazada_implementacion.o

lista_enlazada_main.o: lista_enlazada_main.c lista_enlazada.h
	gcc -c lista_enlazada_main.c

lista_enlazada_implementacion.o: lista_enlazada_implementacion.c lista_enlazada.h
	gcc -c lista_enlazada_implementacion.c

clean:
	-rm lista_enlazada_main.o lista_enlazada_implementacion.o
