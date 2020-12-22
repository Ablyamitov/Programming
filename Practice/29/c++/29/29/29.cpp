#include<iostream>

#include<vector>

#include<string>

#include <map>

#include<ctime>




int main() {

	struct Student 
	{
		std:: string name ;

		int group ;

		std:: map <std::string, int> exams;
	};

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

	one.exams["map_one"] = 5;
	two.exams;
	three.exams;
	four.exams;
	five.exams;
	six.exams;
	seven.exams;
	edge.exams;
	nine.exams;
	ten.exams;



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