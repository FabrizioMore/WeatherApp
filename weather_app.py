import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk


#Creamos la ventana
app = tk.Tk()
app.title('Consulta el Clima!')
app.iconbitmap(r'Weather App\icons\icon.ico')

HEIGHT = 500
WIDTH = 600

#Funciones
def format_response(weather):
    try:
        city = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = f'Ciudad: {str(city)}\nDescripción: {str(description)}\nTemperatura (C°): {str(temp)}'
    
    except:
        final_str = 'There was a problem retrieving that information.'

    return final_str

def get_weather(city):
    weather_key = '340603b461a9ec270c5619c479e1f86c'
    url= 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units':'metric'}
    response = requests.get(url, params=params)
    weather_json = response.json()

    results['text'] = format_response(response.json())

    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)   

def open_image(icon):
    size = int(user_output.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open(f'Weather App/img/{icon}.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img 


#Canvas
canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH,).pack()

background_img = tk.PhotoImage(file=r'Weather App\icons\background.png')
background_label = tk.Label(app, image=background_img)
background_label.place(relwidth=1,relheight=1)

#Casilla de input y botón
user_input = tk.Frame(app, bg='#CDD7D6', bd=5)
user_input.place(relx=0.5, rely=0.1, relwidth=0.75,relheight=0.1, anchor='n')

#Entry
entry = tk.Entry(user_input, bg='#E8EDEC',font=('Roboto',18))
entry.place(relwidth=0.65, relheight=1)

#Botón
button = tk.Button(user_input, text='Consultar', bg='#76938E', font=('Roboto',12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

#Casilla de output
user_output = tk.Frame(app, bg='#CDD7D6', bd=10)
user_output.place(relx=0.5, rely=0.25, relwidth=0.75,relheight=0.6, anchor='n')

#Label
results = tk.Label(user_output, font=('Roboto',18), anchor='nw', justify='left', bd=4)
results.place(relwidth=1, relheight=1)

#Ícono
weather_icon = tk.Canvas(results, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)


app.mainloop()