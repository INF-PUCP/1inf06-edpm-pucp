#include <iostream>
using namespace std;

int main(void) {
	int numero_caracteres;
	cin >> numero_caracteres;
	
	int maximo_ancho;
	cin >> maximo_ancho;
	
	for (int i = 0; i < numero_caracteres; i++) {
		char caracter;
		cin >> caracter;
		cout << caracter;
		if ((i + 1) % maximo_ancho == 0) {
			cout << endl;
		}
	}
	return 0;
}
