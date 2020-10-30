#include<iostream>;
#include<cstring>;
using namespace std;
int main()
{
	setlocale(LC_ALL, "RUS");
	double multi;
	bool check = false;
	string all = "";
	string word;
	string *know =new string[]{ "hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen" };
	for (int i = 0; i < 6;i++)
		all = all + know[i];
	cin >> word;
	double maybe = 1.0;
	for (int i = 0; i < word.length();i++)
	{
		for (int j = 0; j < all.length();j++)
		{
			if (word[i] != all[j])
				continue;
			else
			{
				check = true;
				break;
			}
		}
		if (check)
		{
			multi = double(count(all.begin(), all.end(), word[i])) / double(all.length());
			maybe *= multi;
		}
		else
		{
			cout << 0;
			exit(0);
		}
	}
	cout<< maybe;
}
