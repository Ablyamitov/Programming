#include<iostream>;
#include<cstring>;
using namespace std;

int main()
{
	int  Price, k, n, V, Namecount, mult, v_all, max_counter_v = 0, remember, check_counter = 0, counter_Name;
	string Name = "";
	cin >> n;	//бюджет
	cin >> k;	//количество разновидности выпивки
	int counter[10000];
	int check[1000];
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
	string arrName[1000];
	for (int i = 0; i < k;i++)
	{
		cin >> Name >> Price >> V;
		arrName[i] = Name;
		arrPrice[i] = Price;
		arrV[i] = V;
	}
	cout << arrName[0] << " " << arrPrice[0] << " " << arrV[0];
	for(int i = 0; i<k;i++)
	{	
		if (n >= arrPrice[i])
		{
			mult = 0;
			v_all = 0;
			counter_Name = 0;
			while (n >= Price)
			{
				v_all += arrV[i];
				mult += arrPrice[i];
				counter_Name++;
			}
			counter[i] = v_all - arrV[i];
			mmult[i] = mult - arrPrice[i];
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
			check_counter++;
		}
		else
			continue;
	}
	if (check_counter == 1)
	{
		cout << 21312;
		cout << arrName[remember] << " " << counter_name[remember] << endl;
		cout << counter[remember] << endl;
		cout << n - mmult[remember];
	}
	cout << "Help";
		



}