from django.shortcuts import render
import requests
from .models import City
from django.http import HttpResponse


def index(request):
    cities = City.objects.all()

    API_KEY = '2a8b0f661d6f5cd2819294cf6e03dd3d'
    URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY

    weather_data = []

    for city in cities:
        city_weather = requests.get(
            URL.format(city.name)).json()

        weather = {
            'city': city.name,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
            'country': city_weather['sys']['country']

        }

        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data}

    return render(request, 'blog/index.html', context)
