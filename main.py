from flask import Flask, request, jsonify, render_template
import requests
import random

app = Flask(__name__)

# 10 OpenWeatherMap API keys (hardcoded here)
API_KEYS = [
    "acd4735c9e6224ae1d153f8a61ec7b86",
    "acd4735c9e6224ae1d153f8a61ec7b86",
    "acd4735c9e6224ae1d153f8a61ec7b86",
    "acd4735c9e6224ae1d153f8a61ec7b86",
    "acd4735c9e6224ae1d153f8a61ec7b86",
    "acd4735c9e6224ae1d153f8a61ec7b86",
    "acd4735c9e6224ae1d153f8a61ec7b86",
    "acd4735c9e6224ae1d153f8a61ec7b86",
    "acd4735c9e6224ae1d153f8a61ec7b86",
    "acd4735c9e6224ae1d153f8a61ec7b86"
]

def get_random_api_key():
    return random.choice(API_KEYS)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def weather_by_city():
    city = request.args.get("city")
    lang = request.args.get("lang", "en")

    if not city:
        return jsonify({"error": "City is required"}), 400

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": get_random_api_key(),
        "units": "metric",
        "lang": lang
    }

    r = requests.get(url, params=params)
    if r.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    data = r.json()
    return jsonify({
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"].capitalize(),
        "icon": data["weather"][0]["icon"]
    })


@app.route("/api/geo")
def weather_by_geo():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    lang = request.args.get("lang", "en")

    if not lat or not lon:
        return jsonify({"error": "Latitude and Longitude are required"}), 400

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": get_random_api_key(),
        "units": "metric",
        "lang": lang
    }

    r = requests.get(url, params=params)
    if r.status_code != 200:
        return jsonify({"error": "Location not found"}), 404

    data = r.json()
    return jsonify({
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"].capitalize(),
        "icon": data["weather"][0]["icon"]
    })


@app.route("/api/forecast")
def forecast():
    city = request.args.get("city")
    lang = request.args.get("lang", "en")

    if not city:
        return jsonify({"error": "City is required"}), 400

    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": get_random_api_key(),
        "units": "metric",
        "lang": lang
    }

    r = requests.get(url, params=params)
    if r.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    data = r.json()
    forecast_list = []

    for item in data["list"]:
        forecast_list.append({
            "datetime": item["dt_txt"],
            "temp": item["main"]["temp"],
            "desc": item["weather"][0]["description"].capitalize(),
            "icon": item["weather"][0]["icon"]
        })

    return jsonify({"forecast": forecast_list})


if __name__ == "__main__":
    app.run(debug=True)





# from flask import Flask, request, jsonify, render_template
# import requests
# import os

# app = Flask(__name__)

# API_KEY = os.getenv("WEATHER_API_KEY", "acd4735c9e6224ae1d153f8a61ec7b86")

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/api")
# def weather_by_city():
#     city = request.args.get("city")
#     lang = request.args.get("lang", "en")

#     if not city:
#         return jsonify({"error": "City is required"}), 400

#     url = f"https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric",
#         "lang": lang
#     }

#     r = requests.get(url, params=params)
#     if r.status_code != 200:
#         return jsonify({"error": "City not found"}), 404

#     data = r.json()
#     return jsonify({
#         "city": data["name"],
#         "country": data["sys"]["country"],
#         "temperature": data["main"]["temp"],
#         "feels_like": data["main"]["feels_like"],
#         "humidity": data["main"]["humidity"],
#         "wind_speed": data["wind"]["speed"],
#         "description": data["weather"][0]["description"].capitalize(),
#         "icon": data["weather"][0]["icon"]
#     })


# @app.route("/api/geo")
# def weather_by_geo():
#     lat = request.args.get("lat")
#     lon = request.args.get("lon")
#     lang = request.args.get("lang", "en")

#     if not lat or not lon:
#         return jsonify({"error": "Latitude and Longitude are required"}), 400

#     url = f"https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "lat": lat,
#         "lon": lon,
#         "appid": API_KEY,
#         "units": "metric",
#         "lang": lang
#     }

#     r = requests.get(url, params=params)
#     if r.status_code != 200:
#         return jsonify({"error": "Location not found"}), 404

#     data = r.json()
#     return jsonify({
#         "city": data["name"],
#         "country": data["sys"]["country"],
#         "temperature": data["main"]["temp"],
#         "feels_like": data["main"]["feels_like"],
#         "humidity": data["main"]["humidity"],
#         "wind_speed": data["wind"]["speed"],
#         "description": data["weather"][0]["description"].capitalize(),
#         "icon": data["weather"][0]["icon"]
#     })


# @app.route("/api/forecast")
# def forecast():
#     city = request.args.get("city")
#     lang = request.args.get("lang", "en")

#     if not city:
#         return jsonify({"error": "City is required"}), 400

#     url = f"https://api.openweathermap.org/data/2.5/forecast"
#     params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric",
#         "lang": lang
#     }

#     r = requests.get(url, params=params)
#     if r.status_code != 200:
#         return jsonify({"error": "City not found"}), 404

#     data = r.json()
#     forecast_list = []

#     for item in data["list"]:
#         forecast_list.append({
#             "datetime": item["dt_txt"],
#             "temp": item["main"]["temp"],
#             "desc": item["weather"][0]["description"].capitalize(),
#             "icon": item["weather"][0]["icon"]
#         })

#     return jsonify({"forecast": forecast_list})


# if __name__ == "__main__":
#     app.run(debug=True)




# # from flask import Flask, request, jsonify, render_template
# # import requests

# # app = Flask(__name__)



# # API_KEY = "acd4735c9e6224ae1d153f8a61ec7b86"
# # @app.route('/')
# # def index():
# #     return render_template("index.html")

# # @app.route('/api')
# # def get_weather():
# #     city = request.args.get('city')
# #     if not city:
# #         return jsonify({'error': 'City not provided. Use /api?city=CityName'}), 400

# #     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
# #     response = requests.get(url)
# #     data = response.json()

# #     if response.status_code != 200:
# #         return jsonify({'error': data.get('message', 'Failed to get weather')}), response.status_code

# #     weather_info = {
# #         'city': data['name'],
# #         'country': data['sys']['country'],
# #         'temperature (°C)': data['main']['temp'],
# #         'feels_like (°C)': data['main']['feels_like'],
# #         'description': data['weather'][0]['description'],
# #         'humidity (%)': data['main']['humidity'],
# #         'wind_speed (m/s)': data['wind']['speed']
# #     }

# #     return jsonify(weather_info)

# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=8080)






# # # from flask import Flask, request, jsonify
# # # import requests

# # # app = Flask(__name__)



# # # API_KEY = "acd4735c9e6224ae1d153f8a61ec7b86"
# # # @app.route('/')
# # # def home():
# # #     return "🌦️ Welcome to the Weather API! Use /api?city=CityName"

# # # @app.route('/api')
# # # def get_weather():
# # #     city = request.args.get('city')
# # #     if not city:
# # #         return jsonify({'error': 'City not provided. Use /api?city=CityName'}), 400

# # #     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
# # #     response = requests.get(url)
# # #     data = response.json()

# # #     if response.status_code != 200:
# # #         return jsonify({'error': data.get('message', 'Failed to get weather')}), response.status_code

# # #     weather_info = {
# # #         'city': data['name'],
# # #         'country': data['sys']['country'],
# # #         'temperature (°C)': data['main']['temp'],
# # #         'feels_like (°C)': data['main']['feels_like'],
# # #         'description': data['weather'][0]['description'],
# # #         'humidity (%)': data['main']['humidity'],
# # #         'wind_speed (m/s)': data['wind']['speed']
# # #     }

# # #     return jsonify(weather_info)

# # # if __name__ == '__main__':
# # #     app.run(host='0.0.0.0', port=8080)
