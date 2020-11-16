#ifndef Thirdfile
#define Thirdfile
#include "1.h"
int comb(int k, int n)
{
	return factorial(n) /( factorial(k) * factorial(n - k));	
}
#endif
