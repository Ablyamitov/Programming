#include<iostream>;
#include<math.h>;
using namespace std;
int main()
{
	setlocale(LC_ALL, "RUS");
	int x = 0,k = 0;
	long long n;
	cout << "Введите число: ";
	cin >> n;
	while (pow(2, x) <= n)
	{
		k++;
		x++;
	}
	cout <<endl<< "Количество удовлетворяющих чисел х: " << k;

}