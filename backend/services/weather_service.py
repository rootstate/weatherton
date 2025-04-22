import requests

def fetch_weather(lat: float, lon: float) -> dict:
    """Call open-meteo API and reutrn weather data for param: lat & long"""
    url=(
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
        f"&daily=weather_code,temperature_2m_max,temperature_2m_min"
        f"&timezone=auto"
    )

    # Use requests to call the open-meteo API (HTTP Request)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()