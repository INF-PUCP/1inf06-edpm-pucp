all: ejercicio_2_1_a

ejercicio_2_1_a: ejercicio_2_1_a.o ejercicio_2_1_a_conjunto.o
	gcc -o ejercicio_2_1_a ejercicio_2_1_a.o ejercicio_2_1_a_conjunto.o

ejercicio_2_1_a.o: ejercicio_2_1_a.c ejercicio_2_1_a.h
	gcc -c ejercicio_2_1_a.c

ejercicio_2_1_a_conjunto.o: ejercicio_2_1_a_conjunto.c ejercicio_2_1_a.h
	gcc -c ejercicio_2_1_a_conjunto.c

clean:
	-rm ejercicio_2_1_a.o ejercicio_2_1_a_conjunto.o
