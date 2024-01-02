import requests
import sys

def main():
    while True:
        api_key, location, headers = get_information()
        full_url = construct_url(api_key, location)
        response = requests.get(full_url, headers=headers)
        value, unit = what()
        response1 = response.json()["data"]["values"][value]
        print(f"The {value} is {response1} {unit}")
        continue_or_not_ = input("Do you want to know something else? (y/n) ").strip().lower()
        if continue_or_not_ == "y":
            continue
        elif continue_or_not_ == "n":
            sys.exit("Thank you for using my programm!")
        else:
            sys.exit("Sorry but this is not a valid option. Please restart the programm if you want to retry.")

def get_information(location=None):
    api_key = "API_KEY_HERE" # Replace with your API key from https://app.tomorrow.io/home/
    if location is None:
        location = input("Enter your city: ").capitalize().strip()
    headers = {"accept": "application/json"}
    return api_key, location, headers
    
def construct_url(api_key, location):
    url = "https://api.tomorrow.io/v4/weather/realtime?location=" + location + "&apikey=" + api_key
    return url
    
def what(what_you_wanna_know=None):
    weather_data_map = {
        "cloudbase": ("cloudBase", "m"), "cloudceiling": ("cloudCeiling", "m"), "cloudcover": ("cloudCover", "%"), 
        "dewpoint": ("dewPoint", "°C"), "freezingrainintensity": ("freezingRainIntensity", "mm/h"), "humidity": ("humidity", "%"), 
        "precipitationprobability": ("precipitationProbability", "%"), "pressuresurfacelevel": ("pressureSurfaceLevel", "hPa"), 
        "rainintensity": ("rainIntensity", "mm/h"), "sleetintensity": ("sleetIntensity", "mm/h"), "snowintensity": ("snowIntensity", "mm/h"), 
        "temperature": ("temperature", "°C"), "temperatureapparent": ("temperatureApparent", "°C"), "uvhealthconcern": ("uvHealthConcern", "index"), 
        "uvindex": ("uvIndex", "index"), "visibility": ("visibility", "m"), "weathercode": ("weatherCode", "code"), 
        "winddirection": ("windDirection", "degrees"), "windgust": ("windGust", "m/s"), "windspeed": ("windSpeed", "m/s")
    }

    v = 0
    while v != 3:
        try:
            what_you_wanna_know = input("What do you want to know? ").strip().lower()
            camel_case_value, unit = weather_data_map.get(what_you_wanna_know, (None, None))
            if camel_case_value is None:
                raise ValueError
        except ValueError:
            v += 1
            if v < 3:
                print(f"Sorry but {what_you_wanna_know} is not a valid option. Please try again.")
            else:
                sys.exit("Sorry but you have tried too many times. Please restart the programm if you want to retry.")
        else:
            return camel_case_value, unit

if __name__ == "__main__":
    main()
