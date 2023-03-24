#include <iostream>
using namespace std;

// nombre:     ptr_entero      entero
// valor:      0x7ff7b8a5e6b8  100
// referencia: 0x7ff7b8a5e6b0  0x7ff7b8a5e6b8

int main(void) {
	int entero = 100;
	int* ptr_entero = &entero;

	// 0x7ff7b8a5e6b8
	cout << &entero << endl;

	// 0x7ff7b8a5e6b8
	cout << ptr_entero << endl;

	// 100
	cout << *ptr_entero << endl;

	// 0x7ff7b8a5e6b0
	cout << &ptr_entero << endl;

	// 4 bytes
	cout << sizeof(*ptr_entero) << endl;

	// El tamano del puntero es 8 bytes en mi caso particular.
	// Pueden leer un poco más al respecto en el siguiente enlace:
	// https://stackoverflow.com/a/69997498
	cout << sizeof(ptr_entero) << endl;
	return 0;
}
