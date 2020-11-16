#ifndef Secondheader
#define Secondheader
#include<cmath>
#include "1.h"
double Teylor(double x, int k)
{
	int count = 1;
	double sinx = x;
	while (count <= k)
	{
		sinx += pow(-1, count) * pow(x, (2 * count + 1 )) / factorial(2 * count + 1 );
		count++;
	}
	return sinx;
}
#endif



