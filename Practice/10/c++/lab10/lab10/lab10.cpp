#include<iostream>;
using namespace std;
int main()
{
	long long s, l1, r1, l2, r2;
	setlocale(LC_ALL, "RUS");
	cout << "Введите s,l1,r1,l2,r2: ";
	cin >> s >> l1 >> r1 >> l2 >> r2;
first:
	if ((l1 + r2 == s) || (l1 + l2 == s))
	{
		if (l1 + r2 == s)
			cout << endl << l1 << " " << r2;
		else
			cout << endl << l1 << " " << l2;
	}
	else if (l1 = r1)
		exit(1);
	else
	{
		l1++;
		goto first;
	}
second:
	if ((r1 + r2 == s) || (r1 + l2 == s))
	{
		if (r1 + r2 == s)
			cout << endl << r1 << " " << r2;
		else
			cout << endl << r1 << " " << l2;
	}
	else if (l1 == r1)
		exit(1);
	else
	{
		r1++;
		goto second;
	}
}