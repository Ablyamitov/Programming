#include<iostream>
#include<vector>
#include<ctime>
#include<cmath>
//ГОТОВАЯ ФУНКЦИЯ ДЛЯ МАССИВА ЦЕЛЫХ ЧИСЕЛ(1-ое задание). ДЕЛАЕМ ШАБЛОН, К КОТОРОМУ ПОТОМ БУДЕМ ОБРАЩАТЬСЯ СО ВТОРОЙ(ДВУМЕРНОГО МАССИВА) И ТРЕТЬЕЙ ФУНКЦИИ(3 переменные)
std::vector<int> BozoSort(std::vector<int>a, bool check = true) {
	bool sorted = false;
	while (!sorted) {
		int x1 = rand() % a.size();
		int x2 = rand() % a.size();

		int swap = a[x1];
		a[x1] = a[x2];
		a[x2] = swap;

		sorted = true;
		if (check) {
			for (int i = 1; i < a.size();i++) {
				if (a[i - 1] > a[i]) {
					sorted = false;
					break;
				}
			}
		}
		else {
			for (int i = 1; i < a.size();i++) {
				if (a[i - 1] < a[i]) {
					sorted = false;
					break;
				}
			}
		}
	}

	return a;
}
//2-я функция для двумерного массива
std::vector<int> BozoSort(std::vector < std::vector < int>>a, bool check = true) {
	std::vector<int>help;
	for (int i = 0; i < a.size();i++) {
		for (int j = 0;j < a.size();j++) {
			help.push_back(a[i][j]);
		}
	}
	return BozoSort(help, check);
};

//3-я функция для 3-х переменных
std::vector<int> BozoSort (int first,int second,int third,bool check = true) {
	std::vector<int>three;
	three.push_back(first);
	three.push_back(second);
	three.push_back(third);
	return BozoSort(three, check);
}

int main() {
	srand(time(0));
	std::vector <int> a;
	std::vector <int> temp;
	int n;
	std::cin >> n;
	//1-ое задание - массив целых чисел
	int x;
	for (int i = 0;i < n;i++) {
		std::cin >>x;
		a.push_back(x);
	}
	temp = BozoSort(a);
	std::cout << std::endl;
	for (int i = 0; i < temp.size();i++) {
		std::cout << temp[i]<<" ";
	}
	std::cout<<std::endl;
	bool check;
	temp = BozoSort(a, check = false);
	for (int i = 0; i < temp.size();i++) {
		std::cout << temp[i] << " ";
	}
	//2-е задание - двумерный массив
	std::vector<std::vector<int>> a2;
	int remember = 0;
	for (int i = 0; i < sqrt(n);i++) {
		std::vector<int> temp1;
		for (int j = 0; j < sqrt(n);j++) {
			temp1.push_back(a[remember]);
			remember++;
		}
		a2.push_back(temp1);
		if (remember > n) {
			break;
		}
	}
	temp = BozoSort(a2);
	std::cout << std::endl;
	for (int i = 0; i < temp.size();i++) {
		std::cout << temp[i] << " ";
	}
	temp = BozoSort(a2, check = false);
	std::cout << std::endl;
	for (int i = 0; i < temp.size();i++) {
		std::cout << temp[i] << " ";
	}
	//3-е задание - 3 переменные
	int first = a[0], second=a[1], third=a[2];

	temp = BozoSort(first, second, third);
	std::cout << std::endl;
	for (int i = 0; i < temp.size();i++) {
		std::cout << temp[i] << " ";
	}

	temp = BozoSort(first, second, third, check = false);
	std::cout << std::endl;
	for (int i = 0; i < temp.size();i++) {
		std::cout << temp[i] << " ";
	}
}