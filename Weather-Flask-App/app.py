import json
import requests
from flask import Flask, request, render_template

API_KEY = "YOUR-API-KEY-HERE"
API_HOST = "weatherapi-com.p.rapidapi.com"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_weather', methods=['POST'])
def predict_weather():
    if request.method == 'POST':
        city = request.form['location']  # Get the city name from form input
        API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=06c921750b9a82d8f5d1294e1586276f"
        
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }
        
        try:
            response = requests.get(API_URL, headers=headers)
            json_data = json.loads(response.text)
            
            name = json_data['name']
            region = json_data['sys']['country']
            lat = json_data['coord']['lat']
            lon = json_data['coord']['lon']
            localtime = json_data['dt']
            temp_c = json_data['main']['temp'] - 273.15
            humidity = json_data['main']['humidity']
            wind_speed = json_data['wind']['speed']
            
            return render_template('home.html', name=name, region=region, lat=lat, lon=lon, localtime=localtime,
                                   temp_c=temp_c, humidity=humidity, wind_speed=wind_speed)
        
        except Exception as e:
            print(f"Error fetching weather data: {e}")
            return render_template('home.html', error='Error fetching weather data. Please try again.')

if __name__ == '__main__':
    app.run(debug=True)
#python app.py to run project
#ctrl+F to find a word