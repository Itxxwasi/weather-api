# 🌦️ Weather API + WhatsApp Bot Plugin

A Flask-based Weather API using OpenWeatherMap, deployed on Heroku, with a WhatsApp bot plugin that lets users check current weather conditions by city name or geolocation.

## 🔗 Live API
**Base URL:** `https://weather-apii-8131be613309.herokuapp.com`

---

## 🛠 Features

✅ Real-time weather via OpenWeatherMap  
✅ Get weather by city or geolocation  
✅ 5-day forecast endpoint  
✅ Supports multiple API keys (load balancing)  
✅ Built-in WhatsApp bot plugin (Node.js)  
✅ Urdu & English language support (via `lang` param)

---

## 🖥️ Web UI (Frontend)

The root route `/` serves a weather dashboard with an interactive background, search functionality, and real-time temperature display.

---

## 📦 API Endpoints

### `GET /api?city=<city>&lang=<lang>`
Returns current weather for a city.

Example:
