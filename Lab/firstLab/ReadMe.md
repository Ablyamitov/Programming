<p align="center">МИНИСТЕРСТВО НАУКИ  И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ<br>
Федеральное государственное автономное образовательное учреждение высшего образования<br>
"КРЫМСКИЙ ФЕДЕРАЛЬНЫЙ УНИВЕРСИТЕТ им. В. И. ВЕРНАДСКОГО"<br>
ФИЗИКО-ТЕХНИЧЕСКИЙ ИНСТИТУТ<br>
Кафедра компьютерной инженерии и моделирования</p>
<br>
<h3 align="center">Отчёт по лабораторной работе № 1<br> по дисциплине "Программирование"</h3>
<br><br>
<p>студента 1 курса группы ПИ-б-о-202(1)<br>
Аблямитов Энвер Диляверович<br>
направления подготовки 09.03.04 "Программная инженерия"</p>
<br><br>
<table>
<tr><td>Научный руководитель<br> старший преподаватель кафедры<br> компьютерной инженерии и моделирования</td>
<td>(оценка)</td>
<td>Чабанов В.В.</td>
</tr>
</table>
<br><br>
<p align="center">Симферополь, 2020</p>
<hr>

## Постановка задачи


Разработать сервис предоставляющий данные о погоде в городе Симферополе на момент запроса.  В качестве источника данных о погоде используйте: http://openweathermap.org/. В состав сервиса входит: серверное приложение на языке С++ и клиентское приложение на языке Python.

Серверное приложение (далее Сервер) предназначенное для обслуживания клиентских приложений и минимизации количества запросов к сервису openweathermap.org. Сервер должен обеспечивать возможность получения данных в формате JSON и виде html виджета (для вставки виджета на страницу будет использоваться iframe).

Клиентское приложение должно иметь графический интерфейс отображающий сведения о погоде и возможность обновления данных по требованию пользователя.

Подробности указаны далее.

## Цель работы
1. Закрепить навыки работы с json.
2. Закрепить навыки работы с многофайловыми приложениями.
3. Создать серверное приложение погоды на языке программирования c++.
4. Создать клиентское приложение погоды на языке программирования python.
5. Получить базовое представление о взаимодействии приложений посредством создания клиент-сервеного приложения.

## Выполнение работы

1. Регистрируемся на сайте http://openweathermap.org/. После регистрации генерируем API ключи. 
Мой сгенерированный API ключ: ```e514def49c60c2e57d213dcdf65abb35```.
2. Составляем запрос (пункт I.7) на получение прогноза погоды для Симферополя с почасовым интервалом, в градусах Цельсия, на русском языке.
Мой созданный запрос: ```http://api.openweathermap.org/data/2.5/onecall?lat=44.948237&lon=34.100318&exclude=current,minutely,daily,alerts&appid=e514def49c60c2e57d213dcdf65abb35&units=metric&lang=ru```
3. Составляем запрос (пункт II) для получения времени в Симферополе и изучаем формат ответа. Мой созданный запрос ```http://worldtimeapi.org/api/timezone/Europe/Simferopol```
4. Создаём серверное приложение.
Полный исходный код серверного приложения созданного мною:
```#include <iostream>
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

}```
5. Создаём клиентское приложение.
Полный исходный код клиентского приложения созданного мною:
```from tkinter import *
import json
import requests

											
def ournowweather(event=None): 		#делаем запрос
	try: 		
		answer = requests.get('http://localhost:3000/raw').content.decode("utf8")
		writeanswer = json.loads(answer)

		description.config(text=str(writeanswer["description"]))
		tempreture.config(text=str(round(writeanswer["temp"])) + "°C")
	except requests.exceptions.ConnectionError:		#если не те данные, которые нам нужны
		print("Не могу получить нужные нам данные")
		pass


root = Tk()
root.title("Погода")
root.bind("<Button-3>", ournowweather)
root.geometry("175x250")

		#верхний фрейм Симферопль + описание погоды
Our_location_and_description = Frame(root, bg="#FFD700", height=30)
location = Label(Our_location_and_description, font=("Times New Roman Bold", 12), text="Симферополь", bg="#FFD700",fg="black")
description = Label(Our_location_and_description, font=("Times New Roman", 12), bg="#FFD700", fg="grey")
location.pack(pady=0)
description.pack(pady=0)
Our_location_and_description.pack(side=TOP, fill=X)
		#следующий фрейм огромной температуры 
Our_tempreture = Frame(root, bg="#FFFFFF")
tempreture = Label(Our_tempreture, font=("Arial Bold", 50), bg="#FFFFFF",fg="black")
tempreture.pack(expand=True)
Our_tempreture.pack(expand=True, fill=BOTH)

		#пустой фрейм, чтобы было как в примере
empty_frame_for_exess_space = Frame(root, bg="#FFD700", height=42)
empty_frame_for_exess_space.pack(side=BOTTOM, fill=X)


ournowweather()
root.mainloop()```
6. Скриншот графического интерфейса клиентского приложения созданного мною:

![Рис.1. Скриншот работы клиентского приложения.](./icon/klient.png)

7. Скриншот браузера с загруженными виджетом созданного мною:

![Рис.2. Скриншот работы серверного приложения.](./icon/browser.png)

## Вывод

В ходе лабораторной работы мы:
1. Закрепили навыки работы с json.
2. Закрепили навыки работы с многофайловыми приложениями.
3. Создали серверное приложение погоды на языке программирования c++.
4. Создали клиентское приложение погоды на языке программирования python.
5. Получили базовое представление о взаимодействии приложений посредством создания клиент-сервеного приложения.


