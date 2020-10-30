#include<iostream>;
using namespace std;
int main()
{
	setlocale(LC_ALL, "RUS");
	int k = 0, often_num = 0, red_num = 0,black_num = 0,x;
	int a[37];
	bool are = false;
	for (int i = 0; i <= 36;i++)
		a[i] = 0;
	do
	{
		cin >> x;
		k++;
		if (x > 0 & x < 13)
		{
			if ((x % 2 == 0 || x==11)& x != 12)
				black_num++;
			else
				red_num++;
		}
		else if (x >= 13 & x <= 24)
		{
			if ((x % 2 == 0 || x == 19 || x == 21 || x == 23) & x!=20 &x!=22 & x!=24)
				red_num++;
			else
				black_num++;
		}
		else if ((x >= 25) & (x <= 36))
		{
			if ((x % 2 == 0 || x == 25 || x == 27)&x!=26&x!=28)
				red_num++;
			else
				black_num++;
		}
		a[x] = a[x] + 1;
		if ((x >= 0) & (x <= 36))
		{
			for (int i = 0; i <= 36; i++)
			{
				for (int j = 0; j <= 36;j++)
				{
					if (often_num <= a[j])
						often_num = a[j];
					else
						continue;
				}
				if (a[i] == often_num)
				{
					cout << i << " ";
				}
			}
			cout << endl;
			for (int i = 0; i<=36;i++)
				if (a[i] == 0)
					cout << i << " ";
		}
		if ((x>=0)& (x<=36))
			cout << endl << red_num << " " << black_num << endl<<endl;

	} while ((x >= 0) & (x <= 36));
	exit(0);
}