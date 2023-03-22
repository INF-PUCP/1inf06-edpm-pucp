all: arbol_binario_test

arbol_binario_test: arbol_binario_test.o arbol_binario.o
	gcc -o arbol_binario_test arbol_binario_test.o arbol_binario.o

arbol_binario_test.o: arbol_binario_test.c arbol_binario.h
	gcc -c arbol_binario_test.c

arbol_binario.o: arbol_binario.c arbol_binario.h
	gcc -c arbol_binario.c

clean:
	-rm arbol_binario_test.o arbol_binario.o
