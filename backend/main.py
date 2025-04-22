from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.weather_service import fetch_weather

app = FastAPI()

# Enable CORS for communicatin with frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # Open to all origins to API, change in production!!
    allow_credentials=True,  # Allow cookies or auth hedaers
    allow_methods=["*"],     # Allow all HTTP methods
    allow_headers=["*"],     # Allow any headers
)

@app.get("/")
def read_root():
    return {"message": "Status: live"}

# This decorator binds a URL path to a function (get_weather), {lat} & {lon} are the path paramaters
# FastAPI extracts the paramaters, turns them into floats and passes the to get_weather
@app.get("/weather/{lat}/{lon}")
def get_weather(lat: float, lon: float):
    return fetch_weather(lat, lon)
