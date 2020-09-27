#include<iostream>;
using namespace std;
int main()
{
	setlocale(LC_ALL, "RUS");
	int h1, h2, m1, m2;
	char znak;
	cout << "Введите время первого человека: ";
	cin >> h1 >> znak >> m1;
	if ((0 <= h1)&&(h1 <= 23) && (0 <= m1) && (m1 <= 59))
	{
		cout << endl << "Введите время второго человека: ";
		cin >> h2 >> znak >> m2;
		if ((0 <= h2) &&(h2<= 23) && (0 <= m2) &&(m2<= 59))
		{
			if ((((h2 - h1) == 0) && (abs(m2 - m1) <= 15)) || (((abs(h2 - h1) == 1) && ((m2+60) -m1)<= 15)))
			{
				cout << endl << "Встреча состоится";
			}
			else
			{
				cout << "Встреча не состоится";
			}
		}
		else
		{
			cout<<"Вы ввели неккоректное время, попробуйте изменить значение" << endl;
			return main();
		}
	}
	else
	{
		cout << "Вы ввели неккоректное время, попробуйте изменить значение" << endl;
		return main();
	}
}