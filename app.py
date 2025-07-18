import requests
import matplotlib.pyplot as plt
import seaborn as s
from datetime import datetime

API_KEY = '858ba568d878679b3e5475285de7a551'
CITY = 'London'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)  
data = response.json()  

if 'list' in data:
    dates = []
    temps = []

    for forecast in data['list']:
        dt_txt = forecast['dt_txt']
        temp = forecast['main']['temp']
        dates.append(datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S'))
        temps.append(temp)

    s.set(style="whitegrid")
    plt.figure(figsize=(14,6))
    s.lineplot(x=dates, y=temps, marker='o')

    plt.title(f'5-Day Weather Forecast for {CITY}')
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig('weather_forecast.png')
    print("\n Plot saved as 'weather_forecast.png'")

else:
    print("Message from API:", data.get('message', 'No message provided.'))
