#include<iostream>

#include<vector>

#include<string>

#include <map>

#include<ctime>

#include<iomanip>

using namespace std;

struct Student
{
	string name;

	int group;

	map <string, int> exams;

};

bool operator > (Student one, Student two) {
	return one.name > two.name;
}


ostream& operator << (ostream& out, vector<Student> all_stupid_student)
{
	out << "+------------+-------+------+------+------+------+" << endl << "| Name       | Group | Math | Phys | Hist | Prog |" << endl << "+------------+-------+------+------+------+------+"<<endl;
	for (int i = 0;i< all_stupid_student.size();i++) {
		out << "|"  << all_stupid_student[i].name << setw(14 - all_stupid_student[i].name.size()) << " | " << all_stupid_student[i].group << " "<< "    | " << all_stupid_student[i].exams["math"]<< "    | " << all_stupid_student[i].exams["phys"]<< "    | " << all_stupid_student[i].exams["hist"]<< "    | " << all_stupid_student[i].exams["prog"]<< "    |"<<endl<< "+------------+-------+------+------+------+------+"<<endl;
	}
	return out;
}

ostream& operator << (ostream& out, Student random_stupid_student) {
	out << "+------------+-------+------+------+------+------+"<<endl << "| Name       | Group | Math | Phys | Hist | Prog |" <<endl << "+------------+-------+------+------+------+------+"<<endl << "|"  << random_stupid_student.name << setw(14 - random_stupid_student.name.size()) << " | " << random_stupid_student.group << " " << "    | " << random_stupid_student.exams["math"] << "    | " << random_stupid_student.exams["phys"] << "    | " << random_stupid_student.exams["hist"] << "    | " << random_stupid_student.exams["prog"] << "    |"<<endl << "+------------+-------+------+------+------+------+"<<endl;
	return out;
}


template <class T>
vector <T> BozoSort(vector<T>a) {
	vector<T>forint;
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
		for (int i = 1; i < forint.size();i++) {
			if (forint[i - 1] > forint[i]) {
				sorted = false;
				break;
			}
		}

		return forint;
	}
}

int main() {

	srand(time(NULL));

	vector<Student> all_student,who_have_two ;
	Student one, two, three, four, five, six, seven, edge, nine, ten;
	one.name = "habataitara";
	two.name = "modora";
	three.name = "nai";
	four.name = "to";
	five.name = "itte";
	six.name = "mezashita";
	seven.name = "no";
	edge.name = "ha";
	nine.name = "aoi";
	ten.name = "ano";

	one.group = 3;
	two.group = 2;
	three.group = 3;
	four.group = 2;
	five.group = 1;
	six.group = 4;
	seven.group = 1;
	edge.group = 5;
	nine.group = 4;
	ten.group = 1;

	one.exams["math"] = 5;
	one.exams["phys"] = 5;
	one.exams["hist"] = 5;
	one.exams["prog"] = 5;

	two.exams["math"] = 4;
	two.exams["phys"] = 3;
	two.exams["hist"] = 5;
	two.exams["prog"] = 2;

	three.exams["math"] = 2;
	three.exams["phys"] = 2;
	three.exams["hist"] = 2;
	three.exams["prog"] = 2;

	four.exams["math"] = 3;
	four.exams["phys"] = 5;
	four.exams["hist"] = 2;
	four.exams["prog"] = 5;

	five.exams["math"] = 5;
	five.exams["phys"] = 2;
	five.exams["hist"] = 3;
	five.exams["prog"] = 3;

	six.exams["math"] = 2;
	six.exams["phys"] = 4;
	six.exams["hist"] = 4;
	six.exams["prog"] = 3;

	seven.exams["math"]=4;
	seven.exams["phys"]= 5;
	seven.exams["hist"] =5 ;
	seven.exams["prog"]= 4;

	edge.exams["math"]=5;
	edge.exams["phys"]= 4;
	edge.exams["hist"]= 3;
	edge.exams["prog"]= 2;

	nine.exams["math"] =5;
	nine.exams["phys"] =4;
	nine.exams["hist"] =3;
	nine.exams["prog"] =4;

	ten.exams["math"] =4;
	ten.exams["phys"] =4;
	ten.exams["hist"] =3;
	ten.exams["prog"] =4;

	all_student.push_back(one);
	all_student.push_back(two);
	all_student.push_back(three);
	all_student.push_back(four);
	all_student.push_back(five);
	all_student.push_back(six);
	all_student.push_back(seven);
	all_student.push_back(edge);
	all_student.push_back(nine);
	all_student.push_back(ten);
	
	size_t number_of_students = all_student.size();

	bool if_student_have_two = false;

	for (int i = 0;i< number_of_students;i++)
	{
		if (all_student[i].exams["math"] == 2) {
			if_student_have_two = true;
			who_have_two.push_back(all_student[i]);
			continue;
		}
		else if (all_student[i].exams["phys"] == 2){
			if_student_have_two = true;
			who_have_two.push_back(all_student[i]);
			continue;
		}
		else if (all_student[i].exams["hist"] == 2) {
			if_student_have_two = true;
			who_have_two.push_back(all_student[i]);
			continue;
		}
		else if (all_student[i].exams["prog"] == 2) {
			if_student_have_two = true;
			who_have_two.push_back(all_student[i]);
			continue;
		}
	}
	cout << endl;
	int random_student = rand() % who_have_two.size();
	if (if_student_have_two)
	{
		
		cout << BozoSort(who_have_two);
		cout << endl;
		cout<< "Expulsion";
		cout << endl << endl;
		cout << who_have_two[random_student];
	}
	else
	{
		cout << "Not found";
	}


}
