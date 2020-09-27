#include<iostream>;
using namespace std;
int main()
{
	setlocale(LC_ALL, "RUS");
	long long rez = 1;
	int n;
	cout << "Введите факториал: ";
	cin >> n;
	if (n == 0)
	{
		rez == 1;
	}
	else if (n > 0)
	{
		for (int i = 1; i < n + 1; i++)
		{
			rez *= i;
		}
	}
	else
	{
		cout << "Нужно ввести неотрицательное число, пропробуйте изменить значение" << endl;
		return main();
	}
	cout << "Факториал числа " << n << " = " << rez;
}