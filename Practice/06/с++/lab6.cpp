#include <iostream>;
#include <math.h>;
using namespace std;
int main()
{
	setlocale(LC_ALL, "Rus");

	double a, b, c, x1, x2, d;
	cout << "Уравнение вида: ax^2+bx+c=0" << endl;
	cout << "Введите значение а: ";
	cin >> a;
	cout << endl << "Введите значение b: ";
	cin >> b;
	cout << endl << "Введите значение c: ";
	cin >> c;
	d = b * b - 4 * a * c;
	if ((a == 0) and (b == 0) and (c == 0))
	{
		cout << "Корень - любое число";
	}
	else if (a != 0)
	{
		if ((b == 0) and (c == 0))
		{
			x1 = 0;
			cout << "x1 = " << x1;
		}
		else if (d > 0)
		{
			x1 = (-b + sqrt(d)) / (2 * a);
			x2 = (-b - sqrt(d)) / (2 * a);
			cout << "x1 = " << x1 << endl << "x2 = " << x2 << endl;
		}
		else if (d == 0)
		{
			x1 = -b / (2 * a);

			cout << "x1 = " << x1 << endl;
		}
		else if (d < 0)
		{
			cout << "Нет корней" << endl;
		}
	}
	else if (a == 0)
	{
		if ((b == 0) and (c != 0))
		{
			cout << "Корней нет";
		}
		else if ((b != 0) and (c == 0))
		{
			x1 = 0;
			cout << "x1 = " << x1;
		}
		else
		{
			x1 = -c / b;
			cout << "x1 = " << x1;
		}
	}
}





