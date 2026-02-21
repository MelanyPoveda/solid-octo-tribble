#include<iostream>
using namespace std;

int main (int argc, char *argv[]) {
	string nombre;
	string nombrecompleto;
	int edad;
	string nacimiento;

	
	cout << "Como te llamas\n"; // \n = enter same as python and you also can use endl
	cin >> nombre

	cout << "Digite su nombre completo\n";
	getline(cin, nombrecompleto) // getline is used	to read all the line not only the first word of the reponse of the user
	
	cout << "Cual es tu edad\n";
	cin >> edad;
	
	cout << "En qu" << char(130) << " a" << char(164) << "o naciste\n"; //special characters = char
	cin >> nacimiento;
		
	cout << "\n\n\n\nY se quien eres, eres " << nombre << " y tienenes " << edad << " a" << char(164) << "os";
	return 0;
}



