#include <iostream>
using namespace std;

struct Estructura {
	int atributo;

	// void Saludar(void) {
	// 	cout << "Hola, mi atributo vale " << atributo << endl;
	// }
};


void Saludar(const Estructura& estructura) {
	cout << "Hola, mi atributo vale " << estructura.atributo << endl;
}

int main(void) {
	int* ptr_entero;
	ptr_entero = new int(5);
	cout << "El valor en ptr_entero es " << *ptr_entero << endl;
	delete ptr_entero;
	
	int* arreglo_entero;
	arreglo_entero = new int[5];
	cout << "Cada elemento del arreglo tiene tamano " << sizeof(arreglo_entero[4]) << endl;
	delete[] arreglo_entero;
	
	int* ptr_cien = new int;
	*ptr_cien = 100;
	cout << "El valor de ptr_cien es " << *ptr_cien << endl;
	delete ptr_cien;
	
	Estructura* estructuras = new Estructura[8];
	for (int i = 0; i < 8; i++) {
		Estructura estructura_actual = { i };
		*(estructuras + i) = estructura_actual;
	}
	for (int i = 0; i < 8; i++) {
		// estructuras[i].Saludar();
		Saludar(estructuras[i]);
	}
	delete[] estructuras;
	
	return 0;
}
