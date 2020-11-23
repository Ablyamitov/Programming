#include <iostream>
#include <string>
#include <nlohmann/json.hpp>
#include <cpp_httplib/httplib.h>
#include <fstream>


using namespace httplib;
using json = nlohmann::json;

std::string Shablon;

void gen_response(const Request& req, Response& response) {

	Client worldtimeapi("http://worldtimeapi.org");
	auto res_worldtimeapi = worldtimeapi.Get("/api/timezone/Europe/Simferopol");

	if (!res_worldtimeapi)
	{
		response.set_content("Запрос к серверу времени не удался", "text/plain");
		return;
	}
	else if (res_worldtimeapi->status != 200)
	{

		response.set_content("Ответ сервера времени не 200, а: " + std::to_string(res_worldtimeapi->status), "text/plain");
		return;
	}


	Client openweathermap("http://api.openweathermap.org");
	auto res_openweathermap = openweathermap.Get("/data/2.5/onecall?lat=44.948237&lon=34.100318&exclude=current,minutely,daily,alerts&appid=e514def49c60c2e57d213dcdf65abb35&units=metric&lang=ru");

	if (!res_openweathermap)
	{
		response.set_content("Запрос к серверу погоды не удался", "text/plain");
		return;
	}
	else if (res_openweathermap->status != 200)
	{
		response.set_content("Ответ сервера погоды не 200,а: " + std::to_string(res_openweathermap->status), "text/plain");
		return;
	}


	std::string cache;

	if (cache.empty())
	{
		cache = res_openweathermap->body;
	}

	std::string nowtime;
	nowtime = res_worldtimeapi->body;

	json jcache;
	jcache = json::parse(cache);

	json jtime;
	jtime = json::parse(nowtime);

	bool check = false;
	json remember_way;

	for (int i = 0; i < jcache["hourly"].size(); i++) {
		if (jcache["hourly"][i]["dt"] > jtime["unixtime"]) {
			check = true;
			remember_way = jcache["hourly"][i];
			break;
		}
	}

	if (!check) {
		cache = res_openweathermap->body;
	}

	std::string one = "{hourly[i].weather[0].description}";
	Shablon.replace(Shablon.find(one), one.length(), remember_way["weather"][0]["description"]);

	std::string two = "{hourly[i].weather[0].icon}";
	Shablon.replace(Shablon.find(two), two.length(), remember_way["weather"][0]["icon"]);

	std::string three = "{hourly[i].temp}";
	Shablon.replace(Shablon.find(three), three.length(), std::to_string(int(remember_way["temp"].get<double>())));
	Shablon.replace(Shablon.find(three), three.length(), std::to_string(int(remember_way["temp"].get<double>())));

	response.set_content(Shablon, "text/html");
}



void gen_response_raw(const Request& req, Response& response) {

	Client worldtimeapi("http://worldtimeapi.org");
	auto res_worldtimeapi = worldtimeapi.Get("/api/timezone/Europe/Simferopol");

	if (!res_worldtimeapi)
	{
		response.set_content("Запрос к серверу времени не удался", "text/plain");
		return;
	}
	else if (res_worldtimeapi->status != 200)
	{

		response.set_content("Ответ сервера времени не 200,а: " + std::to_string(res_worldtimeapi->status), "text/plain");
		return;
	}


	Client openweathermap("http://api.openweathermap.org");
	auto res_openweathermap = openweathermap.Get("/data/2.5/onecall?lat=44.948237&lon=34.100318&exclude=current,minutely,daily,alerts&appid=e514def49c60c2e57d213dcdf65abb35&units=metric&lang=ru");

	if (!res_openweathermap)
	{
		response.set_content("Запрос к серверу погоды не удался", "text/plain");
		return;
	}
	else if (res_openweathermap->status != 200)
	{
		response.set_content("Ответ сервера погоды не 200,а: " + std::to_string(res_openweathermap->status), "text/plain");
		return;
	}

	std::string cache;

	if (cache.empty())
	{
		cache = res_openweathermap->body;
	}

	std::string nowtime;
	nowtime = res_worldtimeapi->body;

	json jcache;
	jcache = json::parse(cache);

	json jtime;
	jtime = json::parse(nowtime);

	bool check = false;
	json remember_way;

	for (int i = 0; i < jcache["hourly"].size(); i++) {
		if (jcache["hourly"][i]["dt"] > jtime["unixtime"]) {
			check = true;
			remember_way = jcache["hourly"][i];
			break;
		}
	}

	if (!check) {
		cache = res_openweathermap->body;
	}


	json raw;

	raw["description"] = remember_way["weather"][0]["description"];
	raw["temp"] = remember_way["temp"];

	std::string Raw = raw.dump();
	response.set_content(Raw, "text/json");
}


int main() {

	std::ifstream file("Шаблон погоды.html");
	getline(file, Shablon, '\0');


	Server svr;
	svr.Get("/raw", gen_response_raw);
	std::cout << "Server '/raw' is starting\n";

	svr.Get("/", gen_response);
	std::cout << "Server '/' is starting\n";

	svr.listen("localhost", 3000);

}
