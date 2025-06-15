
from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "5ae194c14e04d2fd22de7c1dcd50124b"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city = "Delhi"
    if request.method == 'POST':
        city = request.form['city']
    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city.title(),
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon'],
                'country': data['sys']['country'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind': data['wind']['speed'],
                'datetime': datetime.now().strftime("%A, %d %B %Y %I:%M %p"),
                'background': data['weather'][0]['main'].lower()
            }
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
