from flask import Flask, jsonify
import requests
import datetime
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (for development purposes)

apikey = 'da0624f409930c0b0031259192832850'

@app.route('/api/weather')
def get_weather():
    try:
        city = "Bangkok"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'
        data = requests.get(url).json()
        weather_des = data['weather'][0]['description']
        temp = data['main']['temp'] - 273.15
        today = datetime.datetime.now().strftime("%Y-%m-%d || %H:%M:%S")
        weather_data = {
            'description': weather_des,
            'temperature': round(temp, 2),
            'timestamp': today
        }
        return jsonify(weather_data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching weather data: {e}'}), 500
    except KeyError as e:
        return jsonify({'error': f'Error parsing weather data: Missing key {e}'}), 500
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True) # รันบนพอร์ต 5000 เพื่อความชัดเจน