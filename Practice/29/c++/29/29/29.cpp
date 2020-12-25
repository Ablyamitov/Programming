#include<iostream>

#include<vector>

#include<string>

#include <map>

#include<ctime>

#include<iomanip>

using namespace std;
struct Student
{
	std::string name;

	int group;

	std::map <std::string, int> exams;

};

ostream& operator << (ostream& out, Student student) {
	out << "+------------+-------+------+------+------+------+\n"
		<< "| Name       | Group | Math | Phys | Hist | Prog |\n"
		<< "+------------+-------+------+------+------+------+\n"
		<< "|" << setw(11) << student.name << " | " << student.group << " "
		<< "    | " << student.exams.at("math")
		<< "    | " << student.exams.at("phys")
		<< "    | " << student.exams.at("hist")
		<< "    | " << student.exams.at("prog")
		<< "    |\n"
		<< "+------------+-------+------+------+------+------+\n";
	return out;
}

ostream& operator << (ostream& out, std::vector<Student> allstruct)
{
	out << "+------------+-------+------+------+------+------+\n"
		<< "| Name       | Group | Math | Phys | Hist | Prog |\n"
		<< "+------------+-------+------+------+------+------+\n";
	for (const auto& Student : allstruct) {
		out << "|" << setw(11) << Student.name << " | " << Student.group << " "
			<< "    | " << Student.exams.at("math")
			<< "    | " << Student.exams.at("phys")
			<< "    | " << Student.exams.at("hist")
			<< "    | " << Student.exams.at("prog")
			<< "    |\n"
			<< "+------------+-------+------+------+------+------+\n";
	}
	return out;
}

bool operator > (Student& a, Student& b) {
	return a.name > b.name;
}

bool operator < (Student& a, Student& b) {
	return a.name < b.name;
}

int main() {

	

	std::vector<Student> allstruct ;
	Student one, two, three, four, five, six, seven, edge, nine, ten;
	one.name = "one";
	two.name = "two";
	three.name = "three";
	four.name = "four";
	five.name = "five";
	six.name = "six";
	seven.name = "seven";
	edge.name = "edge";
	nine.name = "nine";
	ten.name = "ten";


	one.group = 1;
	two.group = 2;
	three.group = 3;
	four.group = 4;
	five.group = 5;
	six.group = 6;
	seven.group = 7;
	edge.group = 8;
	nine.group = 9;
	ten.group = 10;

	one.exams["math"] = 5;
	one.exams["phys"] = 5;
	one.exams["hist"] = 5;
	one.exams["prog"] = 5;

	two.exams["math"] = 4;
	two.exams["phys"] = 3;
	two.exams["hist"] = 5;
	two.exams["prog"] = 2;

	three.exams["math"] = 4;
	three.exams["phys"] = 4;
	three.exams["hist"] = 4;
	three.exams["prog"] = 3;

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



	allstruct.push_back(one);
	allstruct.push_back(two);
	allstruct.push_back(three);
	allstruct.push_back(four);
	allstruct.push_back(five);
	allstruct.push_back(six);
	allstruct.push_back(seven);
	allstruct.push_back(edge);
	allstruct.push_back(nine);
	allstruct.push_back(ten);



}
