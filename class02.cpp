#include <iostream>
#include <mat.h> // library for equations 
using namespace std;

int main (int argc, char *agrv[] ) {

// Variables

  
// No Basic 
string text;

// Basics 

//Text
char caracter = ''; 
// Always ride inside the '' 

// Number with decimals
float numdec; // +- 7 significant figures
double numdoble; // +- 15 significant figure 
// Entire numbre
int numint; // [-2**31 to (2**31)-1]
short numshort; // [-2**15 to (2**15)-1]
long numlong; //  [-2**63 to (2**63)-1]

// bool
bool true; // true = 1
bool false; // false = 0

// constant 
const double PI = 3.14



// Type of equations
int a = 3;
int b = 5;

a + b // addison 
a - b // subtraction 
a * b // multiply 
a / b // division
a % b // modulation 
float (a) / b; // division with decimals
pow ( a , b ); // power
pow ( a.0, 1.0 / b.0 ); // square root
log (a); //logarithm 

return 0;
}
