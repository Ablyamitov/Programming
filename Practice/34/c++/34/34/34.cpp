#include<iostream>
using namespace std;

void create(int **pmas,int n, int x0 = 0, int d = 0) {
    *pmas = new int[n];
     (*pmas)[0] = 0;
   for (int i = 1;i < n;i++) {
        (*pmas)[i] = (*pmas)[i - 1] + d;
    }

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



int* print(int* arr, int n) {
    cout << '[';
    for (int i = 0; i < n;i++) {
        cout << arr[i];
        if (i < n - 1) {
            cout << ", ";
        }
        else {
            cout << ']';
        }
    }
    return arr;
}

void destroy(int **pmas) {
    delete[] *pmas;
    *pmas = nullptr;
}

int main() {
    int n, x0, d;
    int* pmas;
    cin >> n >> x0 >> d;
    create(&pmas,n, x0, d);
    sort(pmas, n);
    print(pmas, n);
    destroy(&pmas);
}