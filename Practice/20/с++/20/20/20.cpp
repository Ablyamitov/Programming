#include<iostream>;
#include<cstring>;
using namespace std;

int main()
{
	int  Price, k, maxPrice = 0, n, V, Namecount, mult, v_all, max_counter_v = 1, remember, check_counter = 0, counter_Name, rePrice;
	string Name = "";
	cin >> n;	//бюджет
	cin >> k;	//количество разновидности выпивки
	int counter[10000];
	int ifcheck1[10000];
	int check[10000];
	int counter_name[10000];
	int arrPrice[10000];
	int arrV[10000];
	for (int i = 0;i <= k - 1;i++)
	{
		counter[i] = 0;
		check[i] = 0;
		counter_name[i] = 0;

	}
	int mmult[10000];
	string arrName[10000];
	for (int i = 0; i < k;i++)
	{
		cin >> Name >> Price >> V;
		arrName[i] = Name;
		arrPrice[i] = Price;
		arrV[i] = V;
	}
	for (int i = 0; i < k;i++)
	{
		if (n >= arrPrice[i])
		{
			rePrice = arrPrice[i];
			mult = rePrice;
			v_all = arrV[i];
			counter_Name = 1;
			for (arrPrice[i];arrPrice[i] <= n;arrPrice[i] += arrPrice[i])
			{
				v_all += arrV[i];
				mult += rePrice;
				counter_Name++;
			}
			counter[i] = v_all;
			mmult[i] = mult;
			counter_name[i] = counter_Name;
			continue;
		}
		else
		{
			counter[i] = 0;
			mmult[i] = n;
			continue;
		}
	}
	for (int i = 0; i <= k - 1;i++)
	{
		if (max_counter_v <= counter[i])
		{
			max_counter_v = counter[i];

		}
		else
			continue;
	}
	for (int i = 0; i <= k - 1;i++)
	{
		if (counter[i] == max_counter_v)
		{
			check[i]++;
			remember = i;
			check_counter = check_counter + 2;
		}
		else
			continue;
	}
	if (check_counter == 1)
	{
		cout << arrName[remember] << " " << counter_name[remember] << endl;
		cout << counter[remember] << endl;
		cout << n - mmult[remember];
	}
	else if (check_counter == 0)
		cout << -1;
	else
	{
		for (int i = 0;i < k;i++)
		{
			if (check[i] == 1)
			{
				ifcheck1[i] = n - arrPrice[i];

			}
			else continue;
		}
		for (int i = 0;i < k;i++)
		{
			if (maxPrice <= ifcheck1[i])
			{
				maxPrice = ifcheck1[i];
				remember = i;
			}
		}
		cout << arrName[remember] << " " << counter_name[remember] << endl;
		cout << counter[remember] << endl;
		cout << n - mmult[remember];
	}
}