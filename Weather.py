import requests
api_address='http://api.openweathermap.org/data/2.5/weather?appid=3cc8b8a0bb673d3ee57d6e40afe09252&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['weather'][0]['main']+':'+json_data['weather'][0]['description']
print(format_add)
