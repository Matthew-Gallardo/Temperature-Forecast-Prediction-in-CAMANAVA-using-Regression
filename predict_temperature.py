# tkinter_app.py

import tkinter as tk
from tkinter import ttk
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('temperature_model.pkl')

# Define the function to make predictions
def predict_temperature():
    # Get selected weather type
    selected_weather = weather_selection.get()
    print("Selected Weather:", selected_weather)

    # Set corresponding weather values
    weather_values = {
        'Clear': [1.0, 0.0, 0.0, 0.0, 0.0],
        'Clouds': [0.0, 1.0, 0.0, 0.0, 0.0],
        'Mist': [0.0, 0.0, 1.0, 0.0, 0.0],
        'Rain': [0.0, 0.0, 0.0, 1.0, 0.0],
        'Smoke': [0.0, 0.0, 0.0, 0.0, 1.0]
    }
    
    if selected_weather in weather_values:
        input_data = pd.DataFrame({
            'main.pressure': [float(entry_pressure.get())],
            'main.humidity': [float(entry_humidity.get())],
            'clouds.all': [float(entry_clouds.get())],
            'wind.speed': [float(entry_wind_speed.get())],
            'weather.Clear': weather_values[selected_weather][0],
            'weather.Clouds': weather_values[selected_weather][1],
            'weather.Mist': weather_values[selected_weather][2],
            'weather.Rain': weather_values[selected_weather][3],
            'weather.Smoke': weather_values[selected_weather][4]  # Adjusted index
        })
        
        print("Input Data:", input_data)  # Debugging print statement
        
        prediction = model.predict(input_data)
        predicted_temperature = float(prediction[0])
        
        result_label.config(text=f"Predicted Temperature: {predicted_temperature:.2f}°C")
    else:
        print("Invalid weather selection")

# Create the main window
root = tk.Tk()
root.title("Temperature Prediction")

# Create and place the input widgets with additional information labels
ttk.Label(root, text="Pressure (hPa):").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_pressure = ttk.Entry(root)
entry_pressure.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Humidity (%):").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_humidity = ttk.Entry(root)
entry_humidity.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Cloudiness (%): ").grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry_clouds = ttk.Entry(root)
entry_clouds.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Wind Speed (m/s): ").grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
entry_wind_speed = ttk.Entry(root)
entry_wind_speed.grid(row=3, column=1, padx=10, pady=5)

# Create and place the "Weather" label
ttk.Label(root, text="Weather:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)

# Create radio buttons for weather selection and adjust position vertically
weather_selection = tk.StringVar()
weather_selection.set('Clear')  # Default selection
weather_types = ['Clear', 'Clouds', 'Mist', 'Rain', 'Smoke']  # Added 'Smoke'
for i, weather_type in enumerate(weather_types):
    ttk.Radiobutton(root, text=weather_type, variable=weather_selection, value=weather_type).grid(row=4+i, column=1, padx=10, pady=5, sticky=tk.W)

# Create and place the predict button
predict_button = ttk.Button(root, text="Predict", command=predict_temperature)
predict_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Create and place the result label
result_label = ttk.Label(root, text="Predicted Temperature: ")
result_label.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
