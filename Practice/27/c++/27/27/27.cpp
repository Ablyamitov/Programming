#include<iostream>
#include<vector>
#include<ctime>

void Coutline(std::vector<int>a, int max, int remember = 0) {
	for (remember; remember < max;remember++) {
		std::cout << a[remember] << " ";
	}
}

std::vector<int> BozoSort(std::vector<int>a,int max) {
	bool sorted = false;
	while (!sorted) {
		int x1 = rand() % max;
		int x2 = rand() % max;

		int swap = a[x1];
		a[x1] = a[x2];
		a[x2] = swap;

		sorted = true;
		
		for (int i = 1; i < max;i++) {
			if (a[i - 1] < a[i]) {
				sorted = false;
				break;
			}
		}
		
	}

	return a;
}


int main() {
	std::vector<int>line;
	std::vector<int>temp;
	int x, n;
	std::cin >> n;

	int max = 0;
	int remember = 0 ;
	for (int i = 0;i <n;i++) {
		std::cin >> x;
		line.push_back(x);
		max++;
		if (max <= 5) {
			temp = BozoSort(line, max);
			Coutline(temp,max, remember);
		}
		else {
			remember = max - 5;
			temp = BozoSort(line, max);
			Coutline(temp, max, remember);
		}
		std::cout <<std::endl ;
	}
}