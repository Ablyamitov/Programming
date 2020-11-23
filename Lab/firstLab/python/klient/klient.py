from tkinter import *
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
root.mainloop()