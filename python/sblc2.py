import datetime
import re
import requests

class Assistant:
    
    def __init__(self):
        self.name = "Jason"
        self.weather_api_key = "b85801988abac35f6e65e7e9daa4925b"  # Replace with your OpenWeatherMap API key
        
        self.current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        self.reminders = []
        
    def greet(self):
        return f"Hello, I am {self.name}. How can I assist you today?"
    
    def get_current_date_time(self):
        self.current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current date is {self.current_date} and time is {self.current_time}."
    
    def get_current_weather(self, city):
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}")
        data = response.json()
        try:
            temp = round((data['main']['temp'] - 273.15) * 9/5 + 32, 2)
            weather = data['weather'][0]['description'].capitalize()
            return f"The current weather in {city} is {temp}°F and {weather}."
        except KeyError:
            return f"Sorry, I couldn't find the weather for {city}."
    
    def get_weather_forecast(self, city):
        response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.weather_api_key}")
        data = response.json()
        forecast = {}
        for i in range(len(data['list'])):
            date_time = datetime.datetime.fromtimestamp(data['list'][i]['dt']).strftime("%Y-%m-%d %H:%M:%S")
            date = date_time.split()[0]
            time = date_time.split()[1]
            temp = round((data['list'][i]['main']['temp'] - 273.15) * 9/5 + 32, 2)
            weather = data['list'][i]['weather'][0]['description'].capitalize()
            if date not in forecast:
                forecast[date] = []
            forecast[date].append(f"At {time}, the temperature will be {temp}°F and {weather}.")
        if forecast:
            result = f"Weather forecast for {city}:\n"
            for date, weather in forecast.items():
                result += date + ":\n"
                for w in weather:
                    result += w + "\n"
            return result
        else:
            return f"Sorry, I couldn't find the weather forecast for {city}. Please try again with a valid city name."
    
    def add_reminder(self, date_time, reminder):
        self.reminders.append((date_time, reminder))
        return f"Reminder added for {date_time}: {reminder}."
    
    def get_reminders(self):
        reminders = ""
        for date_time, reminder in self.reminders:
            reminders += f"{date_time}: {reminder}\n"
        return reminders
    
    def run(self):
        print(self.greet())
        while True:
            command = input("How can I assist you? ")
            if "time" in command:
                print(self.get_current_date_time())
            elif "weather" in command:
                city = input("What city would you like to know the weather for? ")
                if "forecast" in command:
                    forecast = self.get_weather_forecast(city)
                    for date, weather in forecast.items():
                        print(date)
                        for w in weather:
                            print(w)
                else:
                    print(self.get_current_weather(city))
            elif command.startswith("make a reminder"):
                date_time = input("When do you want me to remind you? (YYYY-MM-DD HH:MM:SS) ")
                reminder = input("What do you want me to remind you? ")
                print(self.add_reminder(date_time, reminder))
            elif command == "show reminders":
                reminders = self.get_reminders()
                if reminders:
                    print(reminders)
                else:
                    print("You don't have any reminders.")
            elif command == "exit":
                print("Goodbye!")
                break
            elif command == "continue":
                continue
            else:
                print("Sorry, I don't understand. Please try again.")

assistant = Assistant()
assistant.run()

