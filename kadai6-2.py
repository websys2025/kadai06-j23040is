# kadai6-2.py
# オープンデータ: OpenWeatherMapのAPIを使用して東京の天気を取得
# OpenWeatherMap: https://openweathermap.org/api
# エンドポイント: https://api.openweathermap.org/data/2.5/weather
# 機能: 現在の天気、気温、湿度などの情報を取得可能

import requests

API_KEY = 'e039d8e5e5d192985e243d09e3b777db'
CITY_NAME = 'Tokyo'
URL = 'https://api.openweathermap.org/data/2.5/weather'

params = {
    'q': CITY_NAME,
    'appid': API_KEY,
    'units': 'metric',  # 摂氏で取得
    'lang': 'ja'
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    weather_data = response.json()
    print("天気データ取得成功\n")

    print("都市名:", weather_data['name'])
    print("天気:", weather_data['weather'][0]['description'])
    print("気温:", weather_data['main']['temp'], "°C")
    print("湿度:", weather_data['main']['humidity'], "%")
else:
    print("データ取得失敗:", response.status_code)
