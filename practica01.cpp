#include <iostream>
#include <cmath>

using namespace std;
int main() {
	
	cout << 8 + 7 * 3 + 4 * 6 << endl;
	cout << 3 * (9 * 2/ 100.0) - 5 << endl;
	cout << 1 - 2 - 3 - 4 - 5 << endl; 
	cout << (7 * (10 - 5) * 3 / 100.0) * 4 + 9 << endl;
	cout << 10 / 2.0 * 5 / 1.0 << endl;
	cout << 7 + 3 * 6 / 2.0 - 1 << endl;
	cout << (3 * 9 * (3 + (9 * 3 / (3.0)))) << endl;
	
    float a, b, c;
    a = 6;
	b = 2; 
	c = 3;
	cout << a - b + c  << endl;
	cout << a * b / c << endl;
	cout << a / b * c << endl;
	cout << a * b * c / 100.0 << endl;
	cout << a + b * c / 100.0 << endl;
	cout << a * b / 100.0 * c / 100.0 << endl;
	
	int A, B;
	A = 5; 
	B = A + 6;
	A = A + 1;
	B = A - 5;
	cout << A << endl;
	cout << B << endl;
	
	int q, w, e;
	q = 3;
	w = 20;
	e = q + w;
	w = q + w;
	q = w;
	cout << q << endl;
	cout << w << endl;
	cout << e << endl;
	return 0;
}

