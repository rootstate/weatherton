A sleek web-based weather app built with **FastAPI** (Python backend) and **TypeScript/HTML/CSS** frontend.  
Live weather data powered by the [Open-Meteo API](https://open-meteo.com/).

## Tech Stack
-Layer: Backend
  Python, FastAPI, Uvicorn
-Layer: Frontend
  TypeScript, HTML, CSS
-Layer: API
  Open-Mateo Weather
-Layer: Devtools
  Node.js, TypeScript, Git

## Features
-  **Current temperature** display (°C)
-  Fully decoupled frontend + backend architecture
-  Local TypeScript compilation using `tsc` + user-level Node/npm setup
-  Backend handles all external API calls (no public API exposure)

## Setup and Run
1. Clone repo
git clone https://github.com/rootstate/weatherton.git
cd weatherton

2. Backend setup
cd backend
pip install fastapi uvicorn requests (if not already installed)
go to when uvicorn and fast api are stored
uvicorn main:app -reload
runs att localhost (port 800)

3. Frontend Setup
cd frontend
npm install  # If you have package.json from local tsc install
npx tsc      # compiles app.ts -> dist/app.js

4. Run It
Open frontend/index.html in your browser (can use Live Server or just double click)
