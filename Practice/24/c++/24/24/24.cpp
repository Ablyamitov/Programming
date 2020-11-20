#include<fstream>
#include"json.h"
#include<iostream>
#include<iomanip>
#include<vector>
using nlohmann::json;
using namespace std;
int main()
{
	int complete_work ;
	vector <int>all_userId;
	ifstream in("in.json");
	json inin;
	in >> inin;
	ofstream out("out.json");
	json outout = json::array();
	size_t size_inin = inin.size();
	int maxId;
	for (int i = 0; i < size_inin;i++) {
		all_userId.push_back(inin[i]["userId"]);
	}
	maxId = *max_element(all_userId.begin(), all_userId.end());
	for (int different_id = 1;different_id <= maxId;different_id++) {
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
