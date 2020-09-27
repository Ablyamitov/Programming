#include<iostream>;
#include<math.h>
using namespace std;
int main()
{
	setlocale(LC_ALL, "RUS");
	int a;
	cout << "Введите число: ";
	cin >> a;
	if (a > 1)
	{
		for (int i = 2; i <= sqrt(a); i++)
		{
			if (a % i == 0)
			{
				cout << "Состовное";
				return(0);
			}
		}
		cout << "Простое";
	}
	else
	{
		cout << "Нужно ввести положительное число >1,попробуйте изменить значение" << endl;
		return main();
	}
}