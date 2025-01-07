import requests
# Enter your own api key
Key = "43cbb6412b75cc8573b77b03ebb6f4b5"
def Response(city):
    url = f"https://api.weatherstack.com/current?access_key={Key}"
    a = {"query":city}
    response = requests.get(url,params=a)
    return response
try:


    city = input("Enter the city : ").title()
    response = Response(city)
    if response.status_code ==200:

        r = response.json()
        print(r)
        loaction = r['request']['query']
        temperature = r["current"]["temperature"]
        weather_descriptions = r['current']['weather_descriptions']
        wind_degree = r['current']['wind_degree']
        wind_speed = r['current']['wind_speed']
        pressure = r['current']['pressure']

        print(f"Location : {loaction}\nTemperature : {temperature}\nWeather status : {weather_descriptions}\nWind degree : {wind_degree}\nWind speed : {wind_speed}\nPressure : {pressure}")
    else:
        print(f"error : {response.status_code}")
except ValueError as e:
    print(f"Error : {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Error : {e}")
except KeyError as e:
    print(f"Error : {e}")
except Exception as e:
    print(f"Error : {e}")
