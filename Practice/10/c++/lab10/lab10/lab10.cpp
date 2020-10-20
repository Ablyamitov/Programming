#include <iostream>;
using namespace std;
int main()
{
	setlocale(LC_ALL, "RUS");
	int s, l1, r1, l2, r2,x ;
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
		if (l1 + r2 - s == 0)
		{
			cout << l1 << " " << r2;
		}
		else if (l1 + r2 - s<0)
		{
			x = l1 - (l1 + r2 - s);
			cout << x << " " << r2;
		}
		else if (l1 + r2 - s > 0)
		{
			x = r2 - (l1 + r2 - s);
			cout << l1 << " " << x;
		}
	}
}
