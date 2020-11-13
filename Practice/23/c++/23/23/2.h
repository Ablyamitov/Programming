#ifndef 2_H
#define 2_H
#include "1.h"
#include<cmath>
double Teylor(double x, int k)
{
	int cout == 0;
	double sum == 0.0;
	while (cout <= k)
	{
		if (cout % 2 = !0 && cout != 0)
			sum += (pow(x, k)) / factorial(k);
		cout++;
	}
	return x - sum;
}
#endif

