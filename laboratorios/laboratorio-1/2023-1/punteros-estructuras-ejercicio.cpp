#include <iostream>
// Incluimos cstring para utilizar las funciones strcpy y strlen
// https://cplusplus.com/reference/cstring/
#include <cstring>
using namespace std;

// a. Definimos una estructura
struct Persona {
	char* nombre;
	char* apellido;
	int dni;
	int edad;
	double altura;
	double peso;
};

// c. Crear una funcion para registrar los datos de una persona en una estructura.
void RegistrarDatos(
	Persona*& ptr_persona,
	const char* nombre,
	const char* apellido,
	int dni,
	int edad,
	double altura,
	double peso
) {
	ptr_persona = new Persona();

	ptr_persona->nombre = new char[strlen(nombre) + 1];
	strcpy(ptr_persona->nombre, nombre);

	ptr_persona->apellido = new char[strlen(apellido) + 1];
	strcpy(ptr_persona->apellido, apellido);

	ptr_persona->dni = dni;
	ptr_persona->edad = edad;
	ptr_persona->altura = altura;
	ptr_persona->peso = peso;
}

void PresentarPersona(Persona*& ptr_persona) {
	cout << ptr_persona->nombre << " " << ptr_persona->apellido <<
	" con DNI " << ptr_persona->dni <<
	" tiene " << ptr_persona->edad <<
	" anios, mide " << ptr_persona->altura <<
	" m y pesa " << ptr_persona->peso << " kg." << endl;
}

int main(void) {
	// b. Completar el registro de Jorge Manrique con DNI 12345678
	// de 35 anos, altura 1.62 m y peso 85.53 kg.
	Persona* ptr_persona = new Persona();
	
	// Recordar los member access operators:
	// https://en.cppreference.com/w/cpp/language/operator_member_access
	ptr_persona->nombre = new char[6];
	strcpy(ptr_persona->nombre, "Jorge");

	ptr_persona->apellido = new char[9];
	strcpy(ptr_persona->apellido, "Manrique");

	// Member of pointer
	ptr_persona->dni = 12345678;
	ptr_persona->edad = 35;
	ptr_persona->altura = 1.62;
	// Indireccion
	(*ptr_persona).peso = 85.53;

	PresentarPersona(ptr_persona);

	delete ptr_persona;

	// c. Crear una funcion para registrar los datos de una persona en una estructura.
	Persona* ptr_naruto;
	RegistrarDatos(ptr_naruto, "Naruto", "Uzumaki", 3141592, 19, 1.8, 75.9);
	PresentarPersona(ptr_naruto);
	delete ptr_naruto;

	// d. Crear flujo para ingresar los datos de n personas
	int numero_personas;
	cout << "Ingrese el numero de personas: ";
	cin >> numero_personas;

	Persona** ptr_personas = new Persona*;
	*ptr_personas = new Persona[numero_personas];

	for (int i = 0; i < numero_personas; i++) {
		char* nombre = new char[100];
		char* apellido = new char[100];
		int dni;
		int edad;
		double altura;
		double peso;
		cout << "Persona #" << i + 1 << endl;
		cout << "Ingrese nombre: ";
		cin >> nombre;
		cout << "Ingrese apellido: ";
		cin >> apellido;
		cout << "Ingrese edad: ";
		cin >> edad;
		cout << "Ingrese altura: ";
		cin >> altura;
		cout << "Ingrese peso: ";
		cin >> peso;
		RegistrarDatos(ptr_personas[i], nombre, apellido, dni, edad, altura, peso);
	}

	for (int i = 0; i < numero_personas; i++) {
		PresentarPersona(ptr_personas[i]);
		delete ptr_personas[i];
	}
	delete ptr_personas;

	return 0;
}
