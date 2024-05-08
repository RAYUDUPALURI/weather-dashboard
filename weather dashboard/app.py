from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = 'abc123def456ghi789jkl012mno345pqr'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        print("Error fetching weather data.")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather = get_weather(city)
    return render_template('weather.html', city=city, weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
