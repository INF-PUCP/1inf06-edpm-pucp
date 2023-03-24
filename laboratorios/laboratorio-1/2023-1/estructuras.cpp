#include <iostream>
using namespace std;

struct Fecha {
	int dia;
	int mes;
	int anio;
};

// En el caso de C++, no es necesario usar el keyword struct
// mientras que en C era de uso obligatorio.
// https://stackoverflow.com/a/8423005

void ConsultarYRegistrarFecha(Fecha&);

void ImprimirFecha(const Fecha&);

int main(void) {
	Fecha fecha;
	ConsultarYRegistrarFecha(fecha);
	ImprimirFecha(fecha);
	return 0;
}

// Consulta al usuario la fecha a a ingresar y
// es registrada en la dirección de memoria especificada.
void ConsultarYRegistrarFecha(Fecha& fecha) {
	cout << "Ingrese el dia, el mes y el anio: ";
	cin >> fecha.dia >> fecha.mes >> fecha.anio;
}

// Imprime la fecha especificada en el formato dd/mm/aa.
void ImprimirFecha(const Fecha& fecha) {
	cout << fecha.dia << "/" << fecha.mes << "/" << fecha.anio << endl;
}