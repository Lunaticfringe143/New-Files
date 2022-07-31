from pydoc import classify_class_attrs
import requests
from bs4 import BeautifulSoup
import pandas as pd

#page = requests.get('https://weather.com/en-IN/weather/tenday/l/Nandyal+Andhra+Pradesh?canonicalCityId=651b19bf7cdd3bb2c90d89010bedd07b5c01d113e1907b3665cdb2db15baf603')

#page1 = requests.get('https://www.accuweather.com/en/in/nandyal/186807/weather-forecast/186807')

page2 = requests.get('https://forecast.weather.gov/MapClick.php?lat=35.12894000000006&lon=-117.98562999999996#.YtEuTHZBxnI')
soup = BeautifulSoup(page2.content, 'html.parser')

#print(soup)

week = soup.find(id='seven-day-forecast-container')

#print(week.findall('li'))

items = week.find_all(class_='tombstone-container')

#print(items[0].find(class_='').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

weather_stuff = pd.DataFrame({
	'period': period_names,
	'short_desc': short_description,
	'temp': temperatures,
	})

print(weather_stuff)

weather_stuff.to_csv("weather.csv")
