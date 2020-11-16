#include<iostream>
#include<iomanip>
#include "1.h"
#include "2.h"
#include "3.h"
using namespace std;
int main()
{
	const double PI = 3.141592;
	cout << 'n' << "\t" << "n!" << endl;
	for (int n = 1; n <= 10;n++)
		cout << n << "\t" << factorial(n)<<endl;
	cout << endl;
	cout << 'x' << "\t" << "sin(x)" << endl;
	for (double x = 0; x <= PI / 4; x += PI / 180)
		cout << setprecision(4) << x << "\t" << Teylor(x, 5) << endl;
	cout << endl;
	cout << 'k' << "\t" << "C(k, 10)" << endl;
	for (int k = 1; k<=10; k++)
		cout <<k<<"\t"<< comb(k, 10)<<endl;
}