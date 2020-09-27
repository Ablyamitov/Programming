#include<iostream>;
using namespace std;
int main()
{
	double a, b, d;
	char s;
	setlocale(LC_ALL, "RUS");
	cout << "Введите арифметическое действие: ";
	cin >> a >> s >> b;
	if (s == '+')
	{
		d = a + b;
		cout << d;
	}
	else if (s == '-')
	{
		d = a - b;
		cout << endl << d;
	}
	else if (s == '*')
	{
		d = a * b;
		cout << endl << d;
	}
	else if (s == '/')
	{
		if (b == 0)
		{
			cout << "На 0 делить нельзя!!!!!!!!!!!!!!!!!, попробуйте изменить значение!!!"<<endl;
			return main();
		}
		else
		{
			d = a / b;
			cout << endl << d;
		}
	}
	else
	{
		cout << "Неопознанный знак, пожалуйста, введите корректное значение"<<endl;
		return main ();
	}
		

}