#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

const auto PI = 3.141592653589793;
enum class coord_system {
    Cartesian,
    Polar
};
class Point {
private:
    double a1;
    double a2;
    coord_system coord;
public:
    double remember_a1 , remember_a2 ;
    Point(double a1 = 0, double a2 = 0, coord_system coord = coord_system::Cartesian) :a1(a1), a2(a2), coord(coord) {}
    ~Point() {};

    double get_x() {
        return a1;
    }
    double get_y() {
        return a2;
    }
    double get_r() {
        return sqrt(a1 * a1 + a2 * a2);
    }
    double get_phi() {
        return atan2(a2, a1);
    }
    void set_x(double da1) {
        remember_a1 = get_x();
        a1 = da1;
    }
    void set_y(double da2) {
        remember_a2 = get_y();
        a2 = da2;
    }
    void set_r(double r) {
        a1 = cos(get_phi()) * r;
        a2 = sin(get_phi()) * r;
    }
    void set_phi(double phi) {;
        a1 = cos(phi) * get_r();
        a2 = sin(phi) * get_r();
    }


    bool operator==(Point& other) {
        if (abs(get_x() - other.get_x() < pow(10, -10)) and abs(get_y() - other.get_y() < pow(10, -10)))
            return true;
        else
            return false;
    }
    bool operator!=(Point& other) {
        if (abs(get_x() - other.get_x() > pow(10, -10)) or abs(get_y() - other.get_y() > pow(10, -10)))
            return true;
        else
            return false;
    }





};

istream& operator>>(istream& in, Point& p) {
    double temp_1, temp_2;
    in.ignore(1);
    in >> temp_1;
    p.set_x(temp_1);
    in.ignore(1);
    in >> temp_2;
    p.set_y(temp_2);
    in.ignore(1);
    return in;
}
ostream& operator<<(ostream& out, Point& p) {
    out << '(' << p.get_x() << ',' << p.get_y() << ')';
    return out;
}


int main() {
    std::vector<Point> original;
    std::ifstream fin("data.txt");
    if (!fin.is_open()) {
        std::cout << "Can't open file" << std::endl;
        return 1;
    }
    else {
        while (!fin.eof()) {
            Point p;
            fin >> p;
            fin.ignore(2); // Точки разделены двумя символами ", "
            original.push_back(p);
        }
        fin.close();
    }

    std::vector<Point> simulacrum(original);
    for (auto& p : simulacrum) {
        std::cout << p;
        p.set_x(p.get_x() + 10);
        p.set_phi(p.get_phi() + 180 * PI / 180);
        p.set_y(-p.get_y());
        p.set_x(-p.get_x() - 10);
        std::cout << p << std::endl;
    }

    if (std::equal(original.begin(), original.end(), simulacrum.begin()))
        std::cout << "\nIt works!\n";
    else
        std::cout << "\nIt not works!\n";
}