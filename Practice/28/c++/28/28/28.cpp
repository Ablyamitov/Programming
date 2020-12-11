#include <iostream>
#include<cmath>

bool checknumber(int a, int b) {
    if (a > 1)
    {
        if (a % b == 0)
            return true;
    }
    return false;
}

void print_factorization(unsigned int n){
    int count;
    bool checkall = true;
    bool checkCount;
    int Simple = 2;
    while (checkall)
    {
        count = 0;
        checkCount = checknumber(n,Simple);
        while (checkCount)
        {
            count++;
            n = n / Simple;
            checkCount = checknumber(n, Simple);
        }
        if (count > 0)
        {
            std::cout << Simple;
            if (count > 1)
                std::cout << '^' << count;
            if (n > 1)
               std:: cout << '*';
        }
        Simple++;
        if (n <= 1) 
            checkall = false;
    }
}

int main(){
    int n;
    std::cin >> n;
    print_factorization(n);
}
