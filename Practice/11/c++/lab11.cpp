#include<iostream>;
using namespace std;
int main()
{
	setlocale(LC_ALL, "RUS");
	int i=0,step;
	double a,rez;
	cout << "Введите число, которое хотите возвести в степень: ";
	cin >> a;
	cout << endl << "Введите степень: ";
	cin >> step;

	if (step == 0)
	{
		rez = 1;
	}
	else if (step > 0)
	{
		rez = 1;
		for (; i < step; i++)
		{
			rez *= a;

		}
	}
	else if (step < 0)
	{
		step = -step;
		rez = 1;
		for (; i < step; i++)
		{
			rez *= a;
		}
		rez = 1 / rez;
	}
	cout << rez;
}
