#ifndef Thirdfile
#define Thirdfile
#include "1.h"
int comb(int n, int k)
{
	return factorial(n) /( factorial(k) * factorial(n - k));	
}
#endif
