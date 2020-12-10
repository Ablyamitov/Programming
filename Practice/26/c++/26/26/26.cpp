#include<iostream>
#include<vector>
#include<string>
#include<ctime>
#include<cmath>

template <class T>
void coutrezult(std::vector<T> coutme) {
	std::cout << std::endl;
	for (int i = 0; i < coutme.size();i++) {
		std::cout << coutme[i] << " ";
	}
}

//ПЕРВАЯ ФУНКЦИЯ ДЛЯ ВЕЩЕСТВЕННОГО МАССИВА
template <class T>
std::vector <T> BozoSort(std::vector<T>a, bool check = true){
	std::vector<T>forint;
	for (int i = 0; i < a.size();i++) {
		forint.push_back(a[i]);
	}
	bool sorted = false;
	while (!sorted) {
		int x1 = rand() % forint.size();
		int x2 = rand() % forint.size();

		T swap = forint[x1];
		forint[x1] = forint[x2];
		forint[x2] = swap;

		sorted = true;
		if (check) {
			for (int i = 1; i < forint.size();i++) {
				if (forint[i - 1] > forint[i]) {
					sorted = false;
					break;
				}
			}
		}
		else {
			for (int i = 1; i < forint.size();i++) {
				if (forint[i - 1] < forint[i]) {
					sorted = false;
					break;
				}
			}
		}
	}

	return forint;

}

//ПЕРВАЯ ФУНКЦИЯ ДЛЯ СТРОК

//ВТОРАЯ ФУНКЦИЯ ДЛЯ ВЕЩЕСТВЕННОЙ МАТРИЦЫ
template <class T>
std::vector<T> BozoSort(std::vector < std::vector < T>>a, bool check = true) {
	std::vector<T>help;
	for (int i = 0; i < a.size();i++) {
		for (int j = 0;j < a.size();j++) {
			help.push_back(a[i][j]);
		}
	}
	return BozoSort(help, check);
}





//ТРЕТЬЯ ФУНКЦИЯ ДЛЯ ВЕЩЕСТВЕННЫХ ЧИСЕЛ
template <class T>
std::vector<T> BozoSort(T first, T second, T third, bool check = true) {
	std::vector<T>three;
	three.push_back(first);
	three.push_back(second);
	three.push_back(third);
	return BozoSort(three, check);
}




int main() {
	srand(time(0));
	std::vector <double> a;
	bool check;
	int n;
	std::cin >> n;
	//ПЕРВОЕ ЗАДАНИЕ ДЛЯ ВЕЩЕСТВЕНОГО ВЕКТОРА
	double x;
	for (int i = 0;i < n;i++) {
		std::cin >> x;
		a.push_back(x);
	}
	
	//ПЕРВОЕ ЗАДАНИЕ ДЛЯ СТРОКОВОГО ВЕКТОРА
	std::cout;
	int n1;
	std::cout;
	std::cin >> n1;
	std::vector <std::string> newa;
	std::string newx;
	for (int i = 0;i < n1;i++) {
		std::cin >> newx;
		newa.push_back(newx);
	}

	//ВТОРОЕ ЗАДАНИЕ ДЛЯ ВЕЩЕСТВЕННОЙ МАТРИЦЫ

	std::vector<std::vector<double>> a2;
	int remember = 0;
	for (int i = 0; i < sqrt(n);i++) {
		std::vector<double> temp1;
		for (int j = 0; j < sqrt(n);j++) {
			temp1.push_back(a[remember]);
			remember++;
		}
		a2.push_back(temp1);
		if (remember > n) {
			break;
		}
	}
	
	//ВТОРОЕ ЗАДАНИЕ ДЛЯ СТРОКОВОЙ МАТРИЦЫ

	std::vector<std::vector<std::string>> a22;
	remember = 0;
	for (int i = 0; i < sqrt(n);i++) {
		std::vector<std::string> temp11;
		for (int j = 0; j < sqrt(n);j++) {
			temp11.push_back(newa[remember]);
			remember++;
		}
		a22.push_back(temp11);
		if (remember > n) {
			break;
		}
	}

	//ТРЕТЬЕ ЗАДАНИЕ ДЛЯ ВЕЩЕСТВЕННОЙ МАТРИЦЫ
	double first = a[0], second = a[1], third = a[2];

	//ТРЕТЬЕ ЗАДАНИЕ ДЛЯ СТРОКОВОЙ МАТРИЦЫ
	std::string newfirst = newa[0], newsecond = newa[1], newthird = newa[2];

	
	coutrezult(BozoSort(a));
	
	coutrezult(BozoSort(a, check = false));
	
	
	coutrezult(BozoSort(a2));
	
	coutrezult(BozoSort(a2, check = false));


	coutrezult(BozoSort(first, second, third));

	coutrezult(BozoSort(first, second, third, check = false));

	
	coutrezult(BozoSort(newa));
	
	coutrezult(BozoSort(newa, check = false));


	coutrezult(BozoSort(a22));
	
	coutrezult(BozoSort(a22, check = false));
	

	coutrezult(BozoSort(newfirst, newsecond, newthird));
	
	coutrezult(BozoSort(newfirst, newsecond, newthird, check = false));
	
}




