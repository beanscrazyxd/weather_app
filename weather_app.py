import tkinter as tk
import requests
from tkinter import messagebox

API_KEY = "c970652ed8e6bd353a3c287daffc519f"

# Emoji mapping based on weather descriptions
def get_weather_icon(description):
    desc = description.lower()
    if "cloud" in desc:
        return "☁️"
    elif "rain" in desc:
        return "🌧️"
    elif "clear" in desc:
        return "☀️"
    elif "snow" in desc:
        return "❄️"
    elif "thunder" in desc:
        return "⚡"
    elif "mist" in desc or "fog" in desc:
        return "🌫️"
    else:
        return "🌡️"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"].title()
            icon = get_weather_icon(weather)
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result_label.config(
                text=f"{icon}  Weather in {city.title()}:\n\n"
                     f"☁️  {weather}\n"
                     f"🌡️  Temperature: {temp}°C\n"
                     f"💧  Humidity: {humidity}%\n"
                     f"🌬️  Wind: {wind} m/s"
            )
        else:
            result_label.config(text="⚠️ City not found.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# GUI setup
app = tk.Tk()
app.title("Pretty Weather App")
app.geometry("400x400")
app.configure(bg="#D8F3DC")  # light pastel green

# Title
title_label = tk.Label(app, text="🌤️ Weather App", font=("Helvetica", 18, "bold"), bg="#D8F3DC", fg="#1B4332")
title_label.pack(pady=20)

# City entry
city_entry = tk.Entry(app, font=("Arial", 14), justify="center", bg="#ffffff", fg="black", relief="flat", bd=3)
city_entry.pack(pady=10, ipadx=10, ipady=5)

# Button
get_button = tk.Button(
    app, text="Get Weather", command=get_weather,
    font=("Arial", 12, "bold"), bg="#40916C", fg="black",
    activebackground="#1B4332", activeforeground="white",
    relief="flat", padx=10, pady=5
)
get_button.pack(pady=10)

# Result display
result_label = tk.Label(app, text="", font=("Arial", 13), bg="#D8F3DC", justify="left", fg="#081C15")
result_label.pack(pady=20)

app.mainloop()

