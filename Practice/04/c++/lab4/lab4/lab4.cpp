#include <iostream>
using namespace std;
int main()
{
	int a, b, t;
	setlocale(LC_ALL, "RU");
	cout << "Введите число а: ";
	cin >> a;
	cout << "Введите число b: ";
	cin >> b;
	t = a;
	a = b;
	b = t;
	cout << "a = " << a << endl << "b = " << b << endl;
	cout << "Введите число a: "<<endl;
	cin >> a;
	cout << "Введите число b:"<<endl;
	cin >> b;
	swap(a, b);

	cout << "a = " << a << endl << "b = " << b << endl;
}

