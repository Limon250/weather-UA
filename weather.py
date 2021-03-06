"""

Developed By Limon250

Date of development: 30 October 2019, 21:27:31

Live Weather in Ukraine(without GUI)

Version 1.0

Language: Russian

For using you need to install "pyowm" library

"""


import time
import pyowm

owm = pyowm.OWM('7419d271517c63603aad9ee3c3fc9504')

observation1 = owm.weather_at_place("Vinnytsya")
w1 = observation1.get_weather()
temp1 = w1.get_temperature('celsius')
wind1 = w1.get_wind()
hum1 = w1.get_humidity()
observation2 = owm.weather_at_place('Lutsk')
w2 = observation2.get_weather()
temp2 = w2.get_temperature('celsius')
wind2 = w2.get_wind()
hum2 = w2.get_humidity()
observation3 = owm.weather_at_place('Dnipropetrovsk')
w3 = observation3.get_weather()
temp3 = w3.get_temperature('celsius')
wind3 = w3.get_wind()
hum3 = w3.get_humidity()
observation4 = owm.weather_at_place('Donetsk')
w4 = observation4.get_weather()
temp4 = w4.get_temperature('celsius')
wind4 = w4.get_wind()
hum4 = w4.get_humidity()
observation5 = owm.weather_at_place('Zhytomyr')
w5 = observation5.get_weather()
temp5 = w5.get_temperature('celsius')
wind5 = w5.get_wind()
hum5 = w5.get_humidity()
observation6 = owm.weather_at_place('Uzhhorod')
w6 = observation6.get_weather()
temp6 = w6.get_temperature('celsius')
wind6 = w6.get_wind()
hum6 = w6.get_humidity()
observation7 = owm.weather_at_place('Zaporizhzhya')
w7 = observation7.get_weather()
temp7 = w7.get_temperature('celsius')
wind7 = w7.get_wind()
hum7 = w7.get_humidity()
observation8 = owm.weather_at_place('Ivano-Frankivsk')
w8 = observation8.get_weather()
temp8 = w8.get_temperature('celsius')
wind8 = w8.get_wind()
hum8 = w8.get_humidity()
observation9 = owm.weather_at_place('Kiev')
w9 = observation9.get_weather()
temp9 = w9.get_temperature('celsius')
wind9 = w9.get_wind()
hum9 = w9.get_humidity()
observation_1 = owm.weather_at_place('Kirovohrad')
w_1 = observation_1.get_weather()
temp_1 = w_1.get_temperature('celsius')
wind_1 = w_1.get_wind()
hum_1 = w_1.get_humidity()
observation_2 = owm.weather_at_place('Luhansk')
w_2 = observation_2.get_weather()
temp_2 = w_2.get_temperature('celsius')
wind_2 = w_2.get_wind()
hum_2 = w_2.get_humidity()
observation_3 = owm.weather_at_place('Lviv')
w_3 = observation_3.get_weather()
temp_3 = w_3.get_temperature('celsius')
wind_3 = w_3.get_wind()
hum_3 = w_3.get_humidity()
observation_4 = owm.weather_at_place('Mykolayiv')
w_4 = observation_4.get_weather()
temp_4 = w_4.get_temperature('celsius')
wind_4 = w_4.get_wind()
hum_4 = w_4.get_humidity()
observation_5 = owm.weather_at_place('Odessa')
w_5 = observation_5.get_weather()
temp_5 = w_5.get_temperature('celsius')
wind_5 = w_5.get_wind()
hum_5 = w_5.get_humidity()
observation_6 = owm.weather_at_place('Poltava')
w_6 = observation_6.get_weather()
temp_6 = w_6.get_temperature('celsius')
wind_6 = w_6.get_wind()
hum_6 = w_6.get_humidity()
observation_7 = owm.weather_at_place('Rivne')
w_7 = observation_7.get_weather()
temp_7 = w_7.get_temperature('celsius')
wind_7 = w_7.get_wind()
hum_7 = w_7.get_humidity()
observation_8 = owm.weather_at_place('Sumy')
w_8 = observation_8.get_weather()
temp_8 = w_8.get_temperature('celsius')
wind_8 = w_8.get_wind()
hum_8 = w_8.get_humidity()
observation_9 = owm.weather_at_place('Ternopil')
w_9 = observation_9.get_weather()
temp_9 = w_9.get_temperature('celsius')
wind_9 = w_9.get_wind()
hum_9 = w_9.get_humidity()
observation__1 = owm.weather_at_place('Kharkiv')
w__1 = observation__1.get_weather()
temp__1 = w__1.get_temperature('celsius')
wind__1 = w__1.get_wind()
hum__1 = w__1.get_humidity()
observation__2 = owm.weather_at_place('Kherson')
w__2 = observation__2.get_weather()
temp__2 = w__2.get_temperature('celsius')
wind__2 = w__2.get_wind()
hum__2 = w__2.get_humidity()
observation__3 = owm.weather_at_place('Khmelnytskyy')
w__3 = observation__3.get_weather()
temp__3 = w__3.get_temperature('celsius')
wind__3 = w__3.get_wind()
hum__3 = w__3.get_humidity()
observation__4 = owm.weather_at_place('Cherkasy')
w__4 = observation__4.get_weather()
temp__4 = w__4.get_temperature('celsius')
wind__4 = w__4.get_wind()
hum__4 = w__4.get_humidity()
observation__5 = owm.weather_at_place('Chernihiv')
w__5 = observation__5.get_weather()
temp__5 = w__5.get_temperature('celsius')
wind__5 = w__5.get_wind()
hum__5 = w__5.get_humidity()
observation__6 = owm.weather_at_place('Chernivtsi')
w__6 = observation__6.get_weather()
temp__6 = w__6.get_temperature('celsius')
wind__6 = w__6.get_wind()
hum__6 = w__6.get_humidity()

g1 = ("Винница", "Луцк", "Днепропетровск", "Донецк")
g2 = ("Житомир", "Ужгород", "Запорожье", "Ивано-Франковск")
g3 = ("Киев", "Кировоград", "Луганск", "Львов")
g4 = ("Николаев", "Одесса", "Полтава", "Ровно")
g5 = ("Сумы", "Тернополь", "Харьков", "Херсон")
g6 = ("Хмельницкий", "Черкассы", "Чернигов", "Черновцы")

print(g1)
time.sleep(0.35)
print(g2)
time.sleep(0.35)
print(g3)
time.sleep(0.35)
print(g4)
time.sleep(0.35)
print(g5)
time.sleep(0.35)
print(g6)
time.sleep(1)

s = input("Введите название города из списка выше: ")

if s == "Винница":
	print(w1)
	time.sleep(0.2)
	print(temp1)
	time.sleep(0.2)
	print(wind1)
	time.sleep(0.2)
	print("Осадки: ", hum1)

elif s == "Луцк":
	print(w2)
	time.sleep(0.2)
	print(temp2)
	time.sleep(0.2)
	print(wind2)
	time.sleep(0.2)
	print("Осадки: ", hum2)

elif s == "Днепропетровск":
	print(w3)
	time.sleep(0.2)
	print(temp3)
	time.sleep(0.2)
	print(wind3)
	time.sleep(0.2)
	print("Осадки: ", hum3)

elif s == "Донецк":
	print(w4)
	time.sleep(0.2)
	print(temp4)
	time.sleep(0.2)
	print(wind4)
	time.sleep(0.2)
	print("Осадки: ", hum4)

elif s == "Житомир":
	print(w5)
	time.sleep(0.2)
	print(temp5)
	time.sleep(0.2)
	print(wind5)
	time.sleep(0.2)
	print("Осадки: ", hum5)

elif s == "Ужгород":
	print(w6)
	time.sleep(0.2)
	print(temp6)
	time.sleep(0.2)
	print(wind6)
	time.sleep(0.2)
	print("Осадки: ", hum6)

elif s == "Запорожье":
	print(w7)
	time.sleep(0.2)
	print(temp7)
	time.sleep(0.2)
	print(wind7)
	time.sleep(0.2)
	print("Осадки: ", hum7)

elif s == "Ивано-Франковск":
	print(w8)
	time.sleep(0.2)
	print(temp8)
	time.sleep(0.2)
	print(wind8)
	time.sleep(0.2)
	print("Осадки: ", hum8)

elif s == "Киев":
	print(w9)
	time.sleep(0.2)
	print(temp9)
	time.sleep(0.2)
	print(wind9)
	time.sleep(0.2)
	print("Осадки: ", hum9)

elif s == "Кировоград":
	print(w_1)
	time.sleep(0.2)
	print(temp_1)
	time.sleep(0.2)
	print(wind_1)
	time.sleep(0.2)
	print("Осадки: ", hum_1)

elif s == "Луганск":
	print(w_2)
	time.sleep(0.2)
	print(temp_2)
	time.sleep(0.2)
	print(wind_2)
	time.sleep(0.2)
	print("Осадки: ", hum_2)

elif s == "Львов":
	print(w_3)
	time.sleep(0.2)
	print(temp_3)
	time.sleep(0.2)
	print(wind_3)
	time.sleep(0.2)
	print("Осадки: ", hum_3)

elif s == "Николаев":
	print(w_4)
	time.sleep(0.2)
	print(temp_4)
	time.sleep(0.2)
	print(wind_4)
	time.sleep(0.2)
	print("Осадки: ", hum_4)

elif s == "Одесса":
	print(w_5)
	time.sleep(0.2)
	print(temp_5)
	time.sleep(0.2)
	print(wind_5)
	time.sleep(0.2)
	print("Осадки: ", hum_5)

elif s == "Полтава":
	print(w_6)
	time.sleep(0.2)
	print(temp_6)
	time.sleep(0.2)
	print(wind_6)
	time.sleep(0.2)
	print("Осадки: ", hum_6)

elif s == "Ровно":
	print(w_7)
	time.sleep(0.2)
	print(temp_7)
	time.sleep(0.2)
	print(wind_7)
	time.sleep(0.2)
	print("Осадки: ", hum_7)

elif s == "Сумы":
	print(w_8)
	time.sleep(0.2)
	print(temp_8)
	time.sleep(0.2)
	print(wind_8)
	time.sleep(0.2)
	print("Осадки: ", hum_8)

elif s == "Тернополь":
	print(w_9)
	time.sleep(0.2)
	print(temp_9)
	time.sleep(0.2)
	print(wind_9)
	time.sleep(0.2)
	print("Осадки: ", hum_9)

elif s == "Харьков":
	print(w__1)
	time.sleep(0.2)
	print(temp__1)
	time.sleep(0.2)
	print(wind__1)
	time.sleep(0.2)
	print("Осадки: ", hum__1)

elif s == "Херсон":
	print(w__2)
	time.sleep(0.2)
	print(temp__2)
	time.sleep(0.2)
	print(wind__2)
	time.sleep(0.2)
	print("Осадки: ", hum__2)

elif s == "Хмельницкий":
	print(w__3)
	time.sleep(0.2)
	print(temp__3)
	time.sleep(0.2)
	print(wind__3)
	time.sleep(0.2)
	print("Осадки: ", hum__3)

elif s == "Черкассы":
	print(w__4)
	time.sleep(0.2)
	print(temp__4)
	time.sleep(0.2)
	print(wind__4)
	time.sleep(0.2)
	print("Осадки: ", hum__4)

elif s == "Чернигов":
	print(w__5)
	time.sleep(0.2)
	print(temp__5)
	time.sleep(0.2)
	print(wind__5)
	time.sleep(0.2)
	print("Осадки: ", hum__5)

elif s == "Черновцы":
	print(w__6)
	time.sleep(0.2)
	print(temp__6)
	time.sleep(0.2)
	print(wind__6)
	time.sleep(0.2)
	print("Осадки: ", hum__6)
else:
	print("Такого города нет в базе!")

input()
