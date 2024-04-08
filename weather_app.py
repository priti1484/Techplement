import requests
import time

class WeatherApp:
   def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weatherapi.com/v1/current.json"
        self.favorites = []

      
   def get_weather(self,city):
        response = requests.get(f"{self.base_url}?key={self.api_key}&q={city}")
        return response.json()
   
  
   def add_favorite(self,city):
        if city not in self.favorites:
            self.favorites.append(city)

        
   def update_weather(self):
        while True:
            for city in self.favorites:
                print(self.get_weather(city))
            time.sleep(15)
            
   def run(self):
        while True:
            print("1. Check Weather")
            print("2. Add City to Favorites")
            print("3. View Favorites Cities")
            print("4. Auto Refresh Weather for favorite cities")
            print("5. Exit")
            choice = input("Enter your choice= ")
            
            if choice == "1":
                city = input("Enter city name: ")
                print(self.get_weather(city))
            elif choice == "2":
                city = input("Enter city name: ")
                self.add_favorite(city)
            elif choice == '3':
                print(self.favorites)
            elif choice == "4":
                self.update_weather()
            elif choice == "5":
                break
            else:
                print("Invalid Choice!")
                         
app = WeatherApp('7ecbf160a7cf4ff292d123755240604')
app.run()