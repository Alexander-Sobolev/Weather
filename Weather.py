import pyowm

owm = pyowm.OWM('Token')

place = input("В каком городе?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температура сейчас" + str(temp))

if temp < 10:
    print("Сегодня очень холодно, одевайся тепло!")
elif temp < 20:
    print("Холодно, оденься потеплее!")
else:
    print("На улице жара!")
