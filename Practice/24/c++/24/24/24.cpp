#include<fstream>
#include"json.h"
#include<iostream>
#include<iomanip>
using nlohmann::json;
using namespace std;
int main()
{
	int complete_work = 0;
	ifstream in("in.json");
	json inin;
	in >> inin;
	ofstream out("out.json");
	json outout = json::array();
	size_t size_inin = inin.size();
	int count = 1;
	for (int numsize = 0;numsize < size_inin;numsize++) {
		if (inin[numsize]["userId"] == count) {
			count++;
		}
	}
	for (int different_id = 1;different_id <= count;different_id++) {
		complete_work = 0;
		for (int allwork = 0; allwork <= size_inin;allwork++) {
			if (inin[allwork]["userId"] == different_id && inin[allwork]["completed"])
				complete_work++;
		}
		if (complete_work > 0) {
			outout.push_back(
			{
			{ "task_completed", complete_work },
			{"userId", different_id},
			}
			);
		}
	}
	out << setw(4) << outout << endl;
}
