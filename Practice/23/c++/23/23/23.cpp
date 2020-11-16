#include<iostream>
#include<iomanip>
#include "1.h"
#include "2.h"
#include "3.h"
using namespace std;
int main()
{
	int n,k;
	double x;
	cin >> n;
	cout << factorial(n)<<endl;
	cin >> x >> k;
	cout <<setprecision(4)<< Teylor(x, k)<<endl;
	cin >> n >> k;
	cout << comb(n, k);
}