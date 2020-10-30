#include <iostream>
using namespace std;

double BMI(double weight, double height)
{
	double digit=(weight / (height * height / 10000));
	return digit;
}

void printBMI(double digit)
{
	if (digit < 18.5)
	{
		cout << "Underweight";
	}
	else if ((digit >= 18.5) && (digit < 25))
	{
		cout << "Normal";
	}
	else if ((digit >= 25) && (digit < 30))
	{
		cout << "Overweight";
	}
	else
		cout << "Obesity";
}

int main()
{
	double ves, rost;
	cin >>ves >> rost;
	printBMI(BMI(ves, rost));
}