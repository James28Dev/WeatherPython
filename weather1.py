import requests
import datetime

apikey = 'da0624f409930c0b0031259192832850'

while True:
    city = input("Enter City : ")
    print("------------------------------------")
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'

        data = requests.get(url).json()
        #print(data)

        weather_des = data['weather'][0]['description']
        temp = data['main']['temp'] - 273.15

        today = datetime.datetime.now().strftime("%Y-%m-%d || %H:%M:%S")

        print(today)
        print(f'The weather in {city} is : {weather_des}')
        print(f'The temperature in {city} is : {temp:.2f}')
    except requests.exceptions.RequestException as e:
        print(f"Connection error occurred : {e}")
        print("Please check your internet connection.")
    except KeyError:
            print(f"No weather information found for '{city}' Please check the city name again.")
    except Exception as e:
            print(f"An unexpected error occurred : {e}")
    finally:
        print("------------------------------------")

    option = input("Do you want to close the program? [Y/N] : ").upper()
    if option == 'Y':
        break
    elif option == 'N':
        continue
    else:
        print("Please enter 'Y' or 'N' only. Thank you.")
