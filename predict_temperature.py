
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('temperature_model.pkl')

def predict_temperature():
    selected_weather = weather_selection.get()

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
            'weather.Smoke': weather_values[selected_weather][4]
        })

        print("Input Data:", input_data)

        prediction = model.predict(input_data)
        predicted_temperature = float(prediction[0])

        result_label.config(text=f"{predicted_temperature:.2f}°C")
    else:
        print("Invalid weather selection")

def close_app():
    root.destroy()

def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def on_motion(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

root = tk.Tk()
root.title("Temperature Predictor")
root.configure(bg='white')
root.geometry("300x530")
root.overrideredirect(True)  


root.attributes('-topmost', True)
icon_path = "temp.png"
icon_image = Image.open(icon_path)
icon_image = icon_image.resize((100, 100), Image.ANTIALIAS)
icon_photo = ImageTk.PhotoImage(icon_image)
root.call('wm', 'iconphoto', root._w, icon_photo)

root.bind('<ButtonPress-1>', start_move)
root.bind('<ButtonRelease-1>', stop_move)
root.bind('<B1-Motion>', on_motion)


top_frame = tk.Frame(root, background='white')
top_frame.grid(row=0, column=0, columnspan=3, sticky='ew')

# Title label
tk.Label(top_frame, text="Temperature Predictor", font=("Arial", 16, "bold"), background='white').pack(side=tk.LEFT, padx=10, pady=5)

# Close button
close_button = tk.Label(top_frame, text=" X", font=("Helvetica", 16), fg="black", background='white', cursor="hand2")
close_button.pack(side=tk.RIGHT, padx=10, pady=5)
close_button.bind("<Button-1>", lambda e: close_app())

icon_label = tk.Label(root, image=icon_photo, background='white')
icon_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Predicted Temperature label
tk.Label(root, text="Predicted Temperature:", font=("Helvetica", 12), background='white').grid(row=2, column=0, columnspan=3)
result_label = tk.Label(root, text="0°C", font=("Helvetica", 28, "bold"), background='white')
result_label.grid(row=3, column=0, columnspan=3, pady=5)

# Input fields
tk.Label(root, text="Pressure (hPa):", background='white').grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
entry_pressure = ttk.Entry(root)
entry_pressure.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Humidity (%):", background='white').grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
entry_humidity = ttk.Entry(root)
entry_humidity.grid(row=5, column=1, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Cloudiness (%):", background='white').grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)
entry_clouds = ttk.Entry(root)
entry_clouds.grid(row=6, column=1, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Wind Speed (m/s):", background='white').grid(row=7, column=0, padx=10, pady=5, sticky=tk.E)
entry_wind_speed = ttk.Entry(root)
entry_wind_speed.grid(row=7, column=1, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Weather:", background='white').grid(row=8, column=0, padx=10, pady=5, sticky=tk.E)

# Weather selection
weather_selection = tk.StringVar()
weather_selection.set('Clear')
weather_types = ['Clear', 'Clouds', 'Mist', 'Rain', 'Smoke']

# radio buttons  2x3 grid
tk.Radiobutton(root, text='Clear', variable=weather_selection, value='Clear', background='white').grid(row=8, column=1, padx=5, pady=5, sticky=tk.W)
tk.Radiobutton(root, text='Clouds', variable=weather_selection, value='Clouds', background='white').grid(row=8, column=2, padx=5, pady=5, sticky=tk.W)
tk.Radiobutton(root, text='Mist', variable=weather_selection, value='Mist', background='white').grid(row=9, column=1, padx=5, pady=5, sticky=tk.W)
tk.Radiobutton(root, text='Rain', variable=weather_selection, value='Rain', background='white').grid(row=9, column=2, padx=5, pady=5, sticky=tk.W)
tk.Radiobutton(root, text='Smoke', variable=weather_selection, value='Smoke', background='white').grid(row=10, column=1, padx=5, pady=5, sticky=tk.W)

# Predict button
predict_button = ttk.Button(root, text="Predict", command=predict_temperature)
predict_button.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
