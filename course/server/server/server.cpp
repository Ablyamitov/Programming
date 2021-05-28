﻿#include <iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include <map>
#include <iterator>
#include <nlohmann/json.hpp>
#include <cpp_httplib/httplib.h>


using namespace std;
using namespace httplib;
using json = nlohmann::json;

std::mutex mtx;

struct Game {
	int game_id;
	std::string user1_id;
	bool user1_connected;
	int user1_wins;
	std::string user1_choice;
	std::string user2_id;
	bool user2_connected;
	int user2_wins;
	std::string user2_choice;
};


Game createGame(std::string user1_id) {
	static int id = 0;
	return { id++, user1_id, true, 0,  "", "", false, 0, "" };
}

std::string to_string(const Game& game) {
	std::stringstream ss;
	ss << "{";
	ss << R"("game_id": )" << game.game_id << ",";
	ss << R"("user1_id": ")" << game.user1_id << "\",";
	ss << R"("user2_id": ")" << game.user2_id << "\",";
	ss << R"("user1_connected": )" << (game.user1_connected ? "true" : "false") << ",";
	ss << R"("user2_connected": )" << (game.user2_connected ? "true" : "false") << ",";
	ss << R"("user1_wins": )" << game.user1_wins << ",";
	ss << R"("user2_wins": )" << game.user2_wins << ",";
	ss << R"("user1_choice": ")" << game.user1_choice << "\",";
	ss << R"("user2_choice": ")" << game.user2_choice << "\"";
	ss << "}";
	return ss.str();
}

// Ключ - ID игры
std::map<int, Game> games;
// Ключ - ID user1
std::map<std::string, Game> waiting_games;


void log(std::string msg) {
	std::cout << msg << std::endl;
}

// В этой функции подбираем противников и начинаем игру
void game_search(const Request& req, Response& res) {
	if (req.has_param("ID")) {
		// Достаём из запроса уникальный id клиента
		std::string client_id = req.get_param_value("ID");
		log("Request from client with ID: " + client_id);
		mtx.lock();

		// Если игр ожидающих второго игрока нет, то
		if (waiting_games.size() == 0) {
			// создаём новую игру. 
			waiting_games[client_id] = createGame(client_id);
			log("Create new game with ID: " + std::to_string(waiting_games[client_id].game_id));
			log("Game with ID : " + std::to_string(waiting_games[client_id].game_id) + " waiting from User 2");
			res.set_content(R"({"game_status": "waiting"})", "text/plain; charset=UTF-8");
		}
		else {
			// Если этот клиент создал игру, то
			if (waiting_games.find(client_id) != waiting_games.end()) {
				// проверяем, подключился ли второй игрок
				if (waiting_games[client_id].user2_connected) {
					log("Game with ID : " + std::to_string(waiting_games[client_id].game_id) + " begin");
					// Отправляем клиенту сообщение, что игра началась 
					res.set_content(R"({"game_status": "run", "game_data": )" + to_string(waiting_games[client_id]) + "}", "text/plain; charset=UTF-8");
					// Копируем игру из ожидающих в играющие
					games[waiting_games[client_id].game_id] = waiting_games[client_id];
					// Удаляем из ожидающих
					waiting_games.erase(client_id);
				}
				else {
					// Если второй игрок ещё не подулючился, ждём
					log("Game with ID : " + std::to_string(waiting_games[client_id].game_id) + " waiting from User 2");
					res.set_content(R"({"game_status": "waiting"})", "text/plain; charset=UTF-8");
				}

			}
			else {
				// Если есть ожидающие игры, то берём первую
				Game& game = waiting_games.begin()->second;
				game.user2_id = client_id;
				game.user2_connected = true;
				log("User with ID : " + client_id + " connect to game  " + std::to_string(game.game_id));
				// Отправляем клиенту сообщение, что игра началась 
				res.set_content(R"({"game_status": "run", "game_data": )" + to_string(waiting_games[game.user1_id]) + "}", "text/plain; charset=UTF-8");
			}

		}

		mtx.unlock();
	}
	else {
		log("Request does not contain parameter ID");
		res.set_content("Bad request", "text/plain; charset=UTF-8");
	}
}

int whoWin(std::string u1, std::string u2) {
	if (u1 == u2) return 0; // ничия
	if ((u1 == "rock" && u2 == "scissors") ||
		(u1 == "scissors" && u2 == "paper") ||
		(u1 == "paper" && u2 == "rock")) return 1; // u1
	else return 2; // u2
}

// В этой функции формируем ответ сервера на запрос
void play_game(const Request& req, Response& res) {
	if (req.has_param("ID") && req.has_param("game_id") && req.has_param("user_choice")) {
		std::string user_id = req.get_param_value("ID");
		int game_id = std::stoi(req.get_param_value("game_id"));
		std::string user_choice = req.get_param_value("user_choice");
		mtx.lock();

		if (games.find(game_id) != games.end()) {
			// Пришёл user1
			if (games[game_id].user1_id == user_id) {
				// и user2 ещё не определился
				if (games[game_id].user2_choice == "") {
					games[game_id].user1_choice = user_choice;
					res.set_content(R"({"game_status": "waiting"})", "text/plain; charset=UTF-8");
				}
				else {
					// user1 пришёл после user2 в первый раз
					if (games[game_id].user1_choice == "") {
						games[game_id].user1_choice = user_choice;
						int win = whoWin(games[game_id].user1_choice, games[game_id].user2_choice);
						if (win == 1) res.set_content(R"({"game_status": "run", "winner": "I"})", "text/plain; charset=UTF-8");
						if (win == 2) res.set_content(R"({"game_status": "run", "winner": "Other"})", "text/plain; charset=UTF-8");
						if (win == 0) res.set_content(R"({"game_status": "run", "winner": "Draw"})", "text/plain; charset=UTF-8");
					}
					else {
						// user1 пришёл после user2 НЕ в первый раз
						int win = whoWin(games[game_id].user1_choice, games[game_id].user2_choice);
						if (win == 1) res.set_content(R"({"game_status": "run", "winner": "I"})", "text/plain; charset=UTF-8");
						if (win == 2) res.set_content(R"({"game_status": "run", "winner": "Other"})", "text/plain; charset=UTF-8");
						if (win == 0) res.set_content(R"({"game_status": "run", "winner": "Draw"})", "text/plain; charset=UTF-8");
						games[game_id].user2_choice = "";
						games[game_id].user1_choice = "";
						(win == 1) ? (games[game_id].user1_wins++) : (games[game_id].user2_wins++);
					}
				}


			}
			else {
				// Пришёл user2
				// и user1 ещё не определился
				if (games[game_id].user1_choice == "") {
					games[game_id].user2_choice = user_choice;
					res.set_content(R"({"game_status": "waiting"})", "text/plain; charset=UTF-8");
				}
				else {
					// user2 пришёл после user1 в первый раз
					if (games[game_id].user2_choice == "") {
						games[game_id].user2_choice = user_choice;
						int win = whoWin(games[game_id].user2_choice, games[game_id].user1_choice);
						if (win == 1) res.set_content(R"({"game_status": "run", "winner": "I"})", "text/plain; charset=UTF-8");
						if (win == 2) res.set_content(R"({"game_status": "run", "winner": "Other"})", "text/plain; charset=UTF-8");
						if (win == 0) res.set_content(R"({"game_status": "run", "winner": "Draw"})", "text/plain; charset=UTF-8");
					}
					else {
						// user2 пришёл после user1 НЕ в первый раз
						int win = whoWin(games[game_id].user2_choice, games[game_id].user1_choice);
						if (win == 1) res.set_content(R"({"game_status": "run", "winner": "I"})", "text/plain; charset=UTF-8");
						if (win == 2) res.set_content(R"({"game_status": "run", "winner": "Other"})", "text/plain; charset=UTF-8");
						if (win == 0) res.set_content(R"({"game_status": "run", "winner": "Draw"})", "text/plain; charset=UTF-8");
						games[game_id].user2_choice = "";
						games[game_id].user1_choice = "";
						(win == 1) ? (games[game_id].user2_wins++) : (games[game_id].user1_wins++);
					}
				}
			}
		}
		else {
			log("game not find");
			res.set_content("Bad request", "text/plain; charset=UTF-8");
		}


		mtx.unlock();
	}
	else {
		log("Request does not contain parameter game_id");
		res.set_content("Bad request", "text/plain; charset=UTF-8");
	}

}



void registration(const Request& req, Response& response) {
	json j = json::parse(req.body);
	json file;
	json write_in_file = json::array();

	ifstream read_json("config.json");
	if (!read_json.is_open()) {

		cout << "File to readdddddd is not open\n";
	}
	else {
		cout << "\nFile to readdddd is open\n";
		if (!(read_json.peek() == EOF)) {
			read_json >> file;
			cout << "\nHello\n";
		}
	}
	read_json.close();
	for (int i = 0;i < file.size();i++) {
		write_in_file.push_back(file[i]);
	}

	if (file != "") {
		for (int i = 0;i < file.size();i++) {
			if (file[i]["login"] == j["login"]) {
				cout << "\nЕсть уже такой логин\n";
				response.set_content("", "text/plain");
				return;
			}
		}
	}
	ofstream write_json("config.json");
	if (!write_json.is_open()) {

		cout << "File to write is not open\n";
	}
	else {
		cout << "\nFile to write is open\n";
	}
	//write_in_file.push_back(j);
	int num_id = file.size();
	int id = num_id;
	char c_num;
	string str_id = "";
	int modulo;
	while (num_id != 0) {
		modulo = num_id % 10;
		num_id = num_id / 10;
		c_num = (char)(modulo + 48);
		str_id = c_num + str_id;
	}
	j.push_back({ "coins","0" });
	j.push_back({ "id",str_id });
	write_in_file.push_back(j);
	write_json << setw(4)<< write_in_file;
	write_json.close();
	//size_t last_id = 
	cout << endl << id << endl;
	cout <<endl<< file[id] << endl;
	response.set_content(j.dump(), "text/json; charset=UTF-8");

}

void curr_gen_response(const Request& req, Response& response) {

	std::cout << req.body << "             ";
	json j = json::parse(req.body);
	json write_in_file = json::array();

	
	json file;
	ifstream read_json("config.json");
	if (!read_json.is_open()) {

		cout << "File to read is not open\n";
	}
	else {
		cout << "\nFile to read is open\n";
		if (!(read_json.peek() == EOF)) {
			read_json >> file;
			cout << "\nHello\n";
		}
	}
	read_json.close();
	/*cout << endl << j["login"] << endl;
	cout << endl << j["password"] << endl;
	cout <<endl<< file[0]["login"]<<endl;
	cout << endl << file[0]["password"] << endl;*/

	//std::cout << req.body << "             ";
	for (int i = 0;i < file.size();i++) {
		cout << "\nЗашёл в цикл\n";
		if ((file[i]["password"] == j["password"]) and (file[i]["login"] == j["login"])) {
			//string str = "Нашелся такой человечек c id";
			cout << "\nНашелся такой человечек c id: " << i << '\n';
			
			response.set_content(file[i].dump(), "text/json; charset=UTF-8");
			return;
			//response.set_content(file[i].dump(), "text/json; charset=UTF-8");
		
		}
		else {
			cout << "НЕТ ТАКОГО ЧЕЛА";
			response.set_content("", "text/plain");
		}
	}
	
}



int main() {
	setlocale(LC_ALL, "Rus");
	Server svr;

	svr.Post("/autorizhation", curr_gen_response);
	svr.Post("/registration", registration);
	svr.Post("/game_search", game_search);    // Вызвать функцию gen_response если кто-то обратиться к корню "сайта"
	svr.Post("/play_game", play_game);    // Вызвать функцию gen_response если кто-то обратиться к корню "сайта"
	/*svr.Post("/register", [](const Request& req, Response& response) {
		}
	);*/
	std::cout << "Server '/' is starting\n";

	svr.listen("localhost", 3000);

}