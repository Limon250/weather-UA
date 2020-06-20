"""
Developed by Limon250
Date: 20.06.20 - 21.06.20
Live Weather in Ukraine
Versioj 2.0
Language: Russian
For using you need to install pyowm
"""

import pyowm
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext
import sys
import webbrowser
import time
import pyowm
import time

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

str1 = "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя"

root = Tk()
root.title("Weather in Ukraine")
root.geometry("782x300")


bttns = [
            "Винница", "Луцк", "Днепропетровск", "Донецк",
            "Житомир", "Ужгород", "Запорожье", "Ивано-Франковск",
            "Киев", "Кировоград", "Луганск", "Львов",
            "Николаев", "Одесса", "Полтава", "Ровно",
            "Сумы", "Тернополь", "Харьков", "Херсон",
            "Хмельницкий", "Черкассы", "Чернигов", "Черновцы", "Exit", "C"

        ]

r = 1
c = 0

for i in bttns:
    rel = ""
    cmd = lambda x=i: weather(x)
    ttk.Button(root, text=i, command=cmd, width = 20).grid(row=r, column=c)
    c += 1
    if c > 5:
        c = 0
        r += 1

"""

w_entry = Entry(root, width=132)
w_entry.grid(row=0, column=0, columnspan = 6)

"""

w_entry = scrolledtext.ScrolledText(root, width=95, height=10)
w_entry.grid(row=0, column=0, columnspan=6)

def weather(key):
    if key == "Exit":
        root.after(1, root.destroy)
        sys.exit
    elif key == "C":
        w_entry.delete(1.0, END)
    elif key == "Винница":
        w_entry.insert(END, "Температура: " + str(temp1))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind1))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum1))
        w_entry.insert(END, "\n")
    elif key == "Луцк":
        w_entry.insert(END, "Температура: " + str(temp2))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind2))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum2))
        w_entry.insert(END, "\n")
    elif key == "Днепропетровск":
        w_entry.insert(END, "Температура: " + str(temp3))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind3))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum3))
        w_entry.insert(END, "\n")
    elif key == "Донецк":
        w_entry.insert(END, "Температура: " + str(temp4))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind4))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum4))
        w_entry.insert(END, "\n")
    elif key == "Житомир":
        w_entry.insert(END, "Температура: " + str(temp5))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind5))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum5))
        w_entry.insert(END, "\n")
    elif key == "Ужгород":
        w_entry.insert(END, "Температура: " + str(temp6))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind6))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum6))
        w_entry.insert(END, "\n")
    elif key == "Запорожье":
        w_entry.insert(END, "Температура: " + str(temp7))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind7))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum7))
        w_entry.insert(END, "\n")
    elif key == "Ивано-Франковск":
        w_entry.insert(END, "Температура: " + str(temp8))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind8))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum8))
        w_entry.insert(END, "\n")
    elif key == "Киев":
        w_entry.insert(END, "Температура: " + str(temp9))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind9))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum9))
        w_entry.insert(END, "\n")
    elif key == "Кировоград":
        w_entry.insert(END, "Температура: " + str(temp_1))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind_1))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum_1))
        w_entry.insert(END, "\n")
    elif key == "Луганск":
        w_entry.insert(END, "Температура: " + str(temp_2))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind_2))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum_2))
        w_entry.insert(END, "\n")
    elif key == "Львов":
        w_entry.insert(END, "Температура: " + str(temp_3))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind_3))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum_3))
        w_entry.insert(END, "\n")
    elif key == "Николаев":
        w_entry.insert(END, "Температура: " + str(temp_4))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind_4))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum_4))
        w_entry.insert(END, "\n")
    elif key == "Одесса":
        w_entry.insert(END, "Температура: " + str(temp_5))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind_5))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum_5))
        w_entry.insert(END, "\n")
    elif key == "Полтава":
        w_entry.insert(END, "Температура: " + str(temp_6))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind_6))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum_6))
        w_entry.insert(END, "\n")
    elif key == "Ровно":
        w_entry.insert(END, "Температура: " + str(temp_7))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind_7))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum_7))
        w_entry.insert(END, "\n")
    elif key == "Сумы":
        w_entry.insert(END, "Температура: " + str(temp_8))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind_8))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum_8))
        w_entry.insert(END, "\n")
    elif key == "Тернополь":
        w_entry.insert(END, "Температура: " + str(temp_9))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind_9))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum_9))
        w_entry.insert(END, "\n")
    elif key == "Харьков":
        w_entry.insert(END, "Температура: " + str(temp__1))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind__1))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum__1))
        w_entry.insert(END, "\n")
    elif key == "Херсон":
        w_entry.insert(END, "Температура: " + str(temp__2))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind__2))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum__2))
        w_entry.insert(END, "\n")
    elif key == "Хмельницкий":
        w_entry.insert(END, "Температура: " + str(temp__3))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind__3))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum__3))
        w_entry.insert(END, "\n")
    elif key == "Черкассы":
        w_entry.insert(END, "Температура: " + str(temp__4))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind__4))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum__4))
        w_entry.insert(END, "\n")
    elif key == "Чернигов":
        w_entry.insert(END, "Температура: " + str(temp__5))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind__5))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum__5))
        w_entry.insert(END, "\n")
    elif key == "Черновцы":
        w_entry.insert(END, "Температура: " + str(temp__6))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Ветер: " + str(wind__6))
        time.sleep(0.5)
        w_entry.insert(END, "\n")
        w_entry.insert(END, "Кол-во осадков: " + str(hum__6))
        w_entry.insert(END, "\n")
    else:
        w_entry.insert(END, key)
    
def GH():
    webbrowser.open("https://github.com/Limon250/calc1.0.git")

def Insta():
    webbrowser.open("https://www.instagram.com/___.73th.og___/")

def gl():
    messagebox.showinfo("e-mail", "limon2502003@gmail.com")

def tg():
    messagebox.showinfo("Telegram", "@Ggwpdwp")
def sl():
    webbrowser.open("https://www.sololearn.com/Profile/9212615")

m = Menu(root)
root.config(menu = m)

m1 = Menu(m)
m.add_cascade(label = "Contact Me!", menu=m1)
m1.add_command(label = "Instagramm", command=Insta)
m1.add_command(label = "Gmail", command=gl)
m1.add_command(label = "Telegram", command=tg)

m2 = Menu(m)
m.add_cascade(label = "Source Code", menu=m2)
m2.add_command(label = "Open", command=GH)

m3 = Menu(m)
m.add_cascade(label="SoloLearn", menu=m3)
m3.add_command(label="Open", command=sl)

root.mainloop()