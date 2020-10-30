//не уверен, что работает правильно
#include <iostream>
#include <string>
#include <cmath>
#include <ctime>

using namespace std;

int main()
{
	setlocale(LC_ALL, "RUS");
	srand(time(NULL));

	string password;
	int n, f = 0, a = 1;
	int x;
	bool check = true;

	cout << "Введите количество символов в пароле: ", cin >> n;
	cin >> password;
	string notall = "";
	size_t size_password = password.length();
	string* notpassword = new string[size_password];

	char* symb = new char[size_password];
	string all = "";

	for (int i = 1; i <= n; i++)
		a *= i;
	for (int i = 0;i < size_password;i++)
	{
		for (int j = 0;j < n;j++)
		{
			notall += password[i];
		}
		notpassword[i] = notall;
		notall = "";
	}

	string* allpassword = new string[a];
	for (int i = 0; i <= a - 1; i++)
		allpassword[i] = "";
	if (size_password < n)
	{
		for (int j = 0; j <= (a - 1); j++)
		{
			check = true;
			for (int i = 0; i <= (n - 1); i++)
			{
				x = rand() % size_password;
				all += password[x];
			}
			allpassword[j] = all;
			all = "";
			if (j > 0)
			{
				for (int i = 0;i <= (j - 1);i++)
				{
					if (allpassword[i] == allpassword[j])
					{
						check = false;
						allpassword[j] = "";
						break;
					}
					else
					{
						continue;
					}
				}
				for (int h = 0; h < size_password;h++)
				{
					if (allpassword[j] == notpassword[h])
					{
						check = false;
						allpassword[j] = "";
						break;
					}
					else
						continue;
				}

			}
			if (check)
				cout << allpassword[j] + " ";
			else
			{
				j--;
				continue;
			}
		}
	}
	else
	{
		for (int j = 0; j <= (a - 1); j++)
		{
			check = true;
			for (int i = 0; i <= (n - 1); i++)
			{
				x = rand() % size_password;
				all += password[x];
			}
			allpassword[j] = all;
			for (int h = 0;h <= j - 1;h++)
			{
				if (allpassword[j] == notpassword[h])
				{
					check = false;
					allpassword[j] = "";
					all = "";
					break;
				}
				else continue;

				if (!check)
					break;
			}
			if (check)
			{
				for (int t = 0;t < j;t++)
				{
					if (allpassword[t] == allpassword[j])
					{
						check = false;
						allpassword[j] = "";
						all = "";
						break;
					}
				}
				if (check)
				{
					cout << allpassword[j] + " ";
					all = "";
				}
				else
				{
					j--;
					continue;
				}

			}
			else
			{
				j--;
				continue;
			}
		}
	}
}
