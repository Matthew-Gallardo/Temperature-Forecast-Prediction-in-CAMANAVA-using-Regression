# tkinter_app.py

import tkinter as tk
from tkinter import ttk
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('temperature_model.pkl')

# Define the function to make predictions
def predict_temperature():
    input_data = pd.DataFrame({
        'main.pressure': [float(entry_pressure.get())],
        'main.humidity': [float(entry_humidity.get())],
        'clouds.all': [float(entry_clouds.get())],
        'wind.speed': [float(entry_wind_speed.get())],
        'weather.Clear': [float(entry_clear.get())],
        'weather.Clouds': [float(entry_clouds_weather.get())],
        'weather.Mist': [float(entry_mist.get())],
        'weather.Rain': [float(entry_rain.get())],
        'weather.Smoke': [float(entry_smoke.get())]
    })

    prediction = model.predict(input_data)
    print("Prediction array:", prediction)  # Debugging statement
    predicted_temperature = float(prediction[0])  # Ensure the prediction is a single float value
    print("Predicted Temperature:", predicted_temperature)  # Debugging statement
    
    result_label.config(text=f"Predicted Temperature: {predicted_temperature:.2f}°C")

# Create the main window
root = tk.Tk()
root.title("Temperature Prediction")

# Create and place the input widgets
ttk.Label(root, text="Pressure").grid(row=0, column=0, padx=10, pady=5)
entry_pressure = ttk.Entry(root)
entry_pressure.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Humidity").grid(row=1, column=0, padx=10, pady=5)
entry_humidity = ttk.Entry(root)
entry_humidity.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Clouds").grid(row=2, column=0, padx=10, pady=5)
entry_clouds = ttk.Entry(root)
entry_clouds.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Wind Speed").grid(row=3, column=0, padx=10, pady=5)
entry_wind_speed = ttk.Entry(root)
entry_wind_speed.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(root, text="Weather Clear").grid(row=4, column=0, padx=10, pady=5)
entry_clear = ttk.Entry(root)
entry_clear.grid(row=4, column=1, padx=10, pady=5)

ttk.Label(root, text="Weather Clouds").grid(row=5, column=0, padx=10, pady=5)
entry_clouds_weather = ttk.Entry(root)
entry_clouds_weather.grid(row=5, column=1, padx=10, pady=5)

ttk.Label(root, text="Weather Mist").grid(row=6, column=0, padx=10, pady=5)
entry_mist = ttk.Entry(root)
entry_mist.grid(row=6, column=1, padx=10, pady=5)

ttk.Label(root, text="Weather Rain").grid(row=7, column=0, padx=10, pady=5)
entry_rain = ttk.Entry(root)
entry_rain.grid(row=7, column=1, padx=10, pady=5)

ttk.Label(root, text="Weather Smoke").grid(row=8, column=0, padx=10, pady=5)
entry_smoke = ttk.Entry(root)
entry_smoke.grid(row=8, column=1, padx=10, pady=5)

# Create and place the predict button
predict_button = ttk.Button(root, text="Predict", command=predict_temperature)
predict_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Create and place the result label
result_label = ttk.Label(root, text="Predicted Temperature: ")
result_label.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
