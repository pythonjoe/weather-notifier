import forecastio

API_KEY = "d40e1507c076f3cd3d218fcc1f99b7b8 "
latitude = 35.4868
longitude = 80.8601

forecast = forecastio.load_forecase(API_KEY, latitude, longitude)

byHour = forecast.hourly()

print(byHour)
