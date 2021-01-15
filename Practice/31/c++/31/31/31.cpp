#include<iostream>

#include<vector>

#include <fstream>


using namespace std;

std::ostream& operator << (std::ostream& out, const vector<int>& mass) {
	out << mass.size() << "\t" << "| ";
	for (int i = 0; i < mass.size(); i++) {
		out << &mass[i] << " ";
	}
	out << endl;
	return out;
}

//ЧАСТЬ 3
/*std::ostream& operator << (std::ostream& out, const vector<int> mass) {
	out << mass.size() << "\t" << "| ";
	for (int i = 0; i < mass.size(); i++) {
		out << &mass[i] << " ";						
	}
	out << endl;
	return out;
}*/

int main() {
	vector<int> mass;
	ofstream file;
	file.open("data.txt");
	char symb = 'x';
	size_t vector_size = 63;
	for (int i = 0; i < vector_size;i++) {
		mass.push_back(symb);
		file << mass;
	}
	for (int i = 0;i < vector_size;i++) {
		mass.pop_back();
		file << mass;
	}
	file.close();

}