#include<iostream>
#include "1.h"
#include "2.h"
using namespace std;
int main()
{
	int n,k;
	double x;
	cin >> n;
	cout << factorial(n)<<endl;
	cin >> x >> k;
	cout << Teylor(x, k);
}