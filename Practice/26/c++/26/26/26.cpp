#include<iostream>
#include<vector>
#include<string>
#include<ctime>
#include<cmath>


void coutrezult(std::vector<int> coutme) {
	std::cout << std::endl;
	for (int i = 0; i < coutme.size();i++) {
		std::cout << coutme[i] << " ";
	}
}

//ПЕРВАЯ ФУНКЦИЯ ДЛЯ ВЕЩЕСТВЕННОГО МАССИВА

std::vector <int> BozoSort(std::vector<double>a, bool check = true){
	std::vector<int>forint;
	for (int i = 0; i < a.size();i++) {
		forint.push_back(a[i]);
	}
	bool sorted = false;
	while (!sorted) {
		int x1 = rand() % forint.size();
		int x2 = rand() % forint.size();

		int swap = forint[x1];
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

std::vector <int> BozoSort(std::vector<std::string>a, bool check = true) {
	std::vector<int>convert;
	for (int i = 0; i < a.size();i++) {
		convert.push_back(stoi(a[i]));
	}
	bool sorted = false;
	while (!sorted) {
		int x1 = rand() % convert.size();
		int x2 = rand() % convert.size();

		int swap = convert[x1];
		convert[x1] = convert[x2];
		convert[x2] = swap;

		sorted = true;
		if (check) {
			for (int i = 1; i < convert.size();i++) {
				if (convert[i - 1] > convert[i]) {
					sorted = false;
					break;
				}
			}
		}
		else {
			for (int i = 1; i < convert.size();i++) {
				if (convert[i - 1] < convert[i]) {
					sorted = false;
					break;
				}
			}
		}
	}

	return convert;
}

//ВТОРАЯ ФУНКЦИЯ ДЛЯ ВЕЩЕСТВЕННОЙ МАТРИЦЫ

std::vector<int> BozoSort(std::vector < std::vector < double>>a, bool check = true) {
	std::vector<double>help;
	for (int i = 0; i < a.size();i++) {
		for (int j = 0;j < a.size();j++) {
			help.push_back(a[i][j]);
		}
	}
	return BozoSort(help, check);
};

//ВТОРАЯ ФУНКЦИЯ ДЛЯ ВЕЩЕСТВЕННОЙ СТРОКИ

std::vector<int> BozoSort(std::vector < std::vector < std::string>>a, bool check = true) {
	std::vector<std::string>help;
	for (int i = 0; i < a.size();i++) {
		for (int j = 0;j < a.size();j++) {
			help.push_back(a[i][j]);
		}
	}
	return BozoSort(help, check);
};

//ТРЕТЬЯ ФУНКЦИЯ ДЛЯ ВЕЩЕСТВЕННЫХ ЧИСЕЛ

std::vector<int> BozoSort(double first, double second, double third, bool check = true) {
	std::vector<double>three;
	three.push_back(first);
	three.push_back(second);
	three.push_back(third);
	return BozoSort(three, check);
}

//ТРЕТЬЯ ФУНКЦИЯ ДЛЯ СТРОК

std::vector<int> BozoSort(std::string first, std::string second, std::string third, bool check = true) {
	std::vector<std::string>three;
	three.push_back(first);
	three.push_back(second);
	three.push_back(third);
	return BozoSort(three, check);
}


int main() {
	srand(time(0));
	std::vector <double> a;
	std::vector <int> temp;
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
	std::vector <int> newtemp;
	//1-ое задание - массив целых чисел
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

	temp = BozoSort(a);
	coutrezult(temp);
	temp = BozoSort(a, check = false);
	coutrezult(temp);

	temp = BozoSort(a2);
	coutrezult(temp);
	temp = BozoSort(a2, check = false);
	coutrezult(temp);

	temp = BozoSort(first, second, third);
	coutrezult(temp);
	temp = BozoSort(first, second, third, check = false);
	coutrezult(temp);

	newtemp = BozoSort(newa);
	coutrezult(newtemp);
	newtemp = BozoSort(newa, check = false);
	coutrezult(newtemp);

	newtemp = BozoSort(a22);
	coutrezult(newtemp);
	newtemp = BozoSort(a22, check = false);
	coutrezult(newtemp);

	temp = BozoSort(newfirst, newsecond, newthird);
	coutrezult(temp);
	temp = BozoSort(newfirst, newsecond, newthird, check = false);
	coutrezult(temp);
}




