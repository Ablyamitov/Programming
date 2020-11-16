#ifndef Secondheader
#define Secondheader
#include<cmath>
#include "1.h"
double Teylor(double x, int k)
{
	double rez = x;
	for(int i = 1; i<=k;i++)
	{
		rez += pow(-1, i) * pow(x, (2 * i + 1 )) / factorial(2 * i + 1 );
	}
	return rez;
}
#endif



