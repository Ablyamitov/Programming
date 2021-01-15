#include<iostream>

#include<fstream>

#include<vector>

#include<string>

#include<iomanip>


using namespace std;

struct Passenger {
	unsigned int PassengerId;
	bool Survived;
	unsigned int Pclass;
	string Name;
	string Sex;
	double Age;
	unsigned int SibSp;
	unsigned int Parch;
	string Ticket;
	double Fare;
	string Cabin;
	string Embarked;
}mine;

void sorting(vector<Passenger*> &woman) {
    for (int i = 0; i < woman.size()-1;i++) {
        for (int j = i;j < woman.size();j++) {
            if (woman[i]->Age > woman[j]->Age) {
                swap(*woman[i], *woman[j]);
            }
        }
    }
}


vector<Passenger*> people(vector<Passenger> &passengers) {
    vector<Passenger*> woman;

    for (int i = 0;i < passengers.size();i++ ) {
        if (passengers[i].Survived = true and passengers[i].Sex == "female" and passengers[i].Pclass == 1) {
           woman.push_back(&passengers[i]);
        }
    }
    sorting(woman);
    return woman;
}

std::istream& operator >> (std::istream& file, vector<Passenger>& passengers) {
   


    string str_file;


    bool check = false;

    while (!file.eof()) {

        str_file = "";
        if (!check) {
            std::getline(file, str_file, '\r');           //Удаляем заголовок
            check = true;
        }
        std::getline(file, str_file, ',');            //passengerId
        unsigned int passengerId = stoi(str_file);
        mine.PassengerId = passengerId;

        std::getline(file, str_file, ',');            //Survived
        bool survived = stoi(str_file);
        mine.Survived = survived;



        std::getline(file, str_file, ',');            //Pclass
        unsigned int pclass = stoi(str_file);
        mine.Pclass = pclass;



        std::getline(file, str_file, ',');            //Name
        string name = str_file;
        if (name[name.length() - 1] != '"')      //Если есть запятая в Name , клеим файл
        {
            std::getline(file, str_file, ',');
            name += str_file;
        }
        //name.substr(1, name.length() - 1);
        name.erase(0, 1);                //удаляем первый символ ( _"_ в начале)           
        name.erase(name.size() - 1, 1);    //удаляем последний символ (в конце _"_)
        mine.Name = name;



        std::getline(file, str_file, ',');      //Sex
        mine.Sex = str_file;



        std::getline(file, str_file, ',');      //Age
        if (str_file == "") {
            str_file = "0";
        }
        double age = stoi(str_file);
        mine.Age = age;


        std::getline(file, str_file, ',');      //SibSp
        unsigned int sibSp = stoi(str_file);
        mine.SibSp = sibSp;


        std::getline(file, str_file, ',');      //Parch
        unsigned int parch = stoi(str_file);
        mine.Parch = parch;

        std::getline(file, str_file, ',');      //Ticket
        mine.Ticket = str_file;


        std::getline(file, str_file, ',');      //Fare
        double fare = stoi(str_file);
        mine.Fare = fare;


        std::getline(file, str_file, ',');      //Cabin
        if (str_file == "") {            //Если нету кабины
            str_file = "";
        }
        mine.Cabin = str_file;


        std::getline(file, str_file, '\r');      //Embarked
        mine.Embarked = str_file;
        cout << str_file << endl;
        passengers.push_back(mine);

    }
        return file;
}

std::ostream& operator<< (std::ostream& out, std::vector<Passenger>& passengers) {
    out << "PassengerId\t" << "Survived\t" << "Pclass\t" << "Name\t" << "Sex\t" << "Age\t" << "SibSp\t" << "Parch\t" << "Ticket\t" << "Fare\t" << "Cabin\t" << "Embarked";
    out << endl;
    
    for (int i = 0;i < passengers.size();i++) {
        Passenger& p = passengers[i];
        out << p.PassengerId << "\t" << p.Survived << "\t" << p.Pclass << "\t" << p.Name << "\t" << p.Sex << "\t" << p.Age << "\t" << p.SibSp << "\t" << p.Parch << "\t" << p.Ticket << "\t" << p.Fare << "\t" << p.Cabin << "\t" << p.Embarked << endl;
    }

    return out;
}

       int main() {
           std::ifstream file;
           file.open("train.csv");

           vector<Passenger> passengers;
           file >> passengers;
           people(passengers);
           ofstream csv;
           csv.open("file.csv");
           csv << passengers;
          
       }
