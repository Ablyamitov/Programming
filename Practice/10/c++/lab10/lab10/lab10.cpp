#include <iostream>;
using namespace std;
int main()
{
	setlocale(LC_ALL, "RUS");
	int s, l1, r1, l2, r2, x1, x2;
	cout << "Введите s,l1,r1,l2,r2: ";
	cin >> s >> l1 >> r1 >> l2 >> r2;
	if ((r1 + r2) < s)
	{
		cout << -1;

	}
	else if ((l1 + l2) > s)
	{
		cout << -1;
	}
	else
	{
		if ((r1 + r2) == s)
		{
			cout << r1 << " " << r2;
		}
		else if ((l1 + l2) == s)
		{
			cout << l1 << " " << l2;
		}
		else
		{
			x1 = l1 + s;
			x2 = r2 - s;
			cout << x1 << " " << x2;
		}
	}
}
