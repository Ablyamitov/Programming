#include<iostream>;
using namespace std;
int main()
{
	long long s, l1, r1, l2, r2, x1, x2;
	setlocale(LC_ALL, "RUS");
	cout << "Введите s,l1,r1,l2,r2: ";
	cin >> s >> l1 >> r1 >> l2 >> r2;
	x1 = l1;
	x2 = r2;
	goto poehali;
pribavleniel1:
	x1 = l1 + 1;
	l1 = x1;
poehali:
	if ((x1 + x2 == s) || (x1 + l2 == s))
	{
		if (x1 + x2 == s)
			cout << endl << x1 << " " << x2;
		else
			cout << endl << x1 << " " << l2;
	}
	else if (x2 == l2)
		goto pribavleniel1;
	else if (x1 == r1)
		exit(1);
	else if (x2 == l1)
	{
		x2 = r2 - 1;
		goto poehali;
	}
	else
		cout << endl << "-1";
}