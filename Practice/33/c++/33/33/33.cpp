#include <iostream>
using namespace std;

int* create(int n, int x0 = 0, int d = 0) {
   int* mas = new int[n];
   *mas = x0;
    for (int i = 1;i < n;i++) {
        mas[i] = mas[i - 1] + d;
    }
    return mas;
}



    int* sort(int* arr, int n) {
        for (int i = 0; i < n - 1; i++)
        {
            int key = i + 1;
            auto temp = arr[key];
            for (int j = i + 1; j > 0; j--)
            {
                if (temp < arr[j - 1])
                {
                    arr[j] = arr[j - 1];
                    key = j - 1;
                }
            }
            arr[key] = temp;
        }
        return arr;
    }

    int * print(int *arr,int n) {
        cout << '[';
        for (int i = 0; i < n;i++) {
            cout << arr[i];
            if (i < n-1) {
                cout << ", ";
            }
            else {
                cout << ']';
            }
        }
        return arr;
    }

int main(){
    int n,x0,d;
    cin >> n>>x0>>d;
    int *mas = create(n,x0,d);
    sort(mas, n);
    print(mas, n);
    delete[] mas;
}

