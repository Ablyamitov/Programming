#include<string>;
#include<iostream>;
using namespace std;
int main()
{
	char x1, x2, x3, x4, x5, x6, x7, x8, x9;
	int n;
	bool k = true;
	string ticket;
	cin >> n;
	for (int i = 1;i <= n;i++)
	{
		cin >> x1 >> x2 >> x3 >> x4 >> x5 >> x6 >> x7 >> x8 >> x9;
		if ((x1 == 'a') and (x5 == '5') and (x6 == '5') and (x7 == '6') and (x8 == '6') and (x9 == '1'))
		{
			char arr[9] = { x1,x2,x3,x4,x5,x6,x7,x8,x9 };
			for (int j = 0;j <= 8;j++)
				ticket += arr[j];
			cout << ticket << "";
			ticket = '\0';
			k = false;
		}
		else
			continue;
	}
	if (k)
		cout << -1;
}