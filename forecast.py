import urllib.request
import json

API_KEY = '50227a41393f890c497f3b019385a950'
URL_API = "http://api.openweathermap.org/data/2.5/forecast/daily?q="
DAYS = 14


def forecast(city):

    summary = {}

    max_temp = []
    min_temp = []
    weather = []

    url = URL_API + city + '&cnt=' + str(DAYS) + '&APPID=' + API_KEY

    request = urllib.request.Request(url)

    response = urllib.request.urlopen(request)

    data = json.loads(response.read().decode('utf-8'))

    for day in range(DAYS):
        max_temp.append(data['list'][day]['temp']['max'])
        min_temp.append(data['list'][day]['temp']['min'])
        weather.append(data['list'][day]['weather'][0]['description'])

        summary = {'city': city, 'max_temp': max_temp, 'min_temp': min_temp, 'forecast': weather}

    return summary


if __name__ == '__main__':

    try:
        forecast('Stockholm')
    except IOError:
        print('no internet connection')
