import pyowm

owm = pyowm.OWM('a27b65aa4c7aefdb7e7bbb7f87e07d24' )



place = input("Enter your city/country: ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print(w)
print("Temperature is" + str(temp))

if temp < 10:
    print("Weather  little bit cold ")

elif temp > 20:
    print("Weather is normal dress up you want")

