const fetchWeather = async () => {
    const lat = (document.getElementById("lat") as HTMLInputElement).value;
    const lon = (document.getElementById("lon") as HTMLInputElement).value;

    const url = `http://localhost:8000/weather/${lat}/${lon}`;
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("Failed to fetch");

        const data = await response.json();

        const temp = data.current?.temperature_2m || data.current_weather?.temperature || "--";
        (document.getElementById("temperature") as HTMLElement).textContent = temp.toString();
    } catch (err) {
        console.error("Weather fetch failed:", err);
        (document.getElementById("temperature") as HTMLElement).textContent = "Error";
    }
};

document.getElementById("fetchWeather")?.addEventListener("click", fetchWeather);
