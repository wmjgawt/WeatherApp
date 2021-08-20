import requests
from tkinter import*


def get_weather(canvas):
    city = textentry.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=dfda755ef505e6dc586f16142f20943d"
    json_data = requests.get(api).json()
    main = json_data["weather"][0]["main"]
    temperature = int(1.8*(json_data["main"]["temp"]-273)+32)
    feels = int(1.8*(json_data["main"]["feels_like"]-273)+32)
    max = int(1.8*(json_data["main"]["temp_max"] - 273)+32)
    min = int(1.8*(json_data["main"]["temp_min"] - 273)+32)

    final = main
    other = "temperature : " + str(temperature) + " F \n" + "feels like : " + str(feels) + " F \n" + "max temp : " + str(max) + " F \n" + "min temp : " + str(min) +" F"
    label1.config(text=final)
    label2.config(text=other)


canvas = Tk()
canvas.geometry("600x600")
canvas.title("Weather App")

a = ("cambria", 15, "bold")
b = ("cambria", 35, "bold")

textentry = Entry(canvas, font=b, )
textentry.pack(pady=20)
textentry.focus()
textentry.bind("<Return>", get_weather)

label1 = Label(canvas, font=a)
label1.pack()
label2 = Label(canvas, font=a)
label2.pack()

canvas.mainloop()
