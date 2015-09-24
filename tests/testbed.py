import pywapi

temp = pywapi.get_weather_from_weather_com('15213', 'imperial')
print temp['forecasts'][0]['high']
print temp['current_conditions']['temperature']
#{'units': {'distance': u'mi', 'speed': u'mph', 'temperature': u'F', 'rainfall': u'in', 'pressure': u'in'}, 
#'current_conditions': {'moon_phase': {'text': u'Waxing Gibbous', 'icon': u'9'}, 
#'last_updated': u'9/23/15 7:25 PM EDT', 
#'temperature': u'71', 
#'dewpoint': u'53', 
#'text': u'Clear', 
#'uv': {'index': u'0', 'text': u'Low'}, 
#'visibility': u'9.0', 
#'humidity': u'52', 
#'station': u'Pittsburgh, PA, US', 
#'barometer': {'direction': u'steady', 'reading': u'30.23'}, 
#'feels_like': u'71', 
#'wind': {'gust': u'N/A', 'direction': u'20', 'speed': u'5', 'text': u'NNE'}, 
#'icon': u'31'}, 
#'location': {'lat': u'40.44', 'lon': u'-79.96', 'name': u'Pittsburgh, PA (15213)'}, 
#'forecasts': [{'day_of_week': u'Wednesday', 'high': u'71', 'sunset': u'7:16 PM', 'low': u'52', 'night': {'brief_text': u'Clear', 'text': u'Clear', 'chance_precip': u'0', 'humidity': u'75', 'wind': {'gust': u'N/A', 'direction': u'52', 'speed': u'5', 'text': u'NE'}, 'icon': u'31'}, 'date': u'Sep 23', 'day': {'brief_text': u'', 'text': u'', 'chance_precip': u'0', 'humidity': u'0', 'wind': {'gust': u'N/A', 'direction': u'0', 'speed': u'calm', 'text': u'CALM'}, 'icon': u''}, 'sunrise': u'7:08 AM'}, {'day_of_week': u'Thursday', 'high': u'83', 'sunset': u'7:16 PM', 'low': u'55', 'night': {'brief_text': u'M Clear', 'text': u'Mostly Clear', 'chance_precip': u'0', 'humidity': u'62', 'wind': {'gust': u'N/A', 'direction': u'82', 'speed': u'7', 'text': u'E'}, 'icon': u'33'}, 'date': u'Sep 24', 'day': {'brief_text': u'Sunny', 'text': u'Sunny', 'chance_precip': u'0', 'humidity': u'50', 'wind': {'gust': u'N/A', 'direction': u'71', 'speed': u'9', 'text': u'ENE'}, 'icon': u'32'}, 'sunrise': u'7:08 AM'}, {'day_of_week': u'Friday', 'high': u'80', 'sunset': u'7:16 PM', 'low': u'56', 'night': {'brief_text': u'M Cloudy', 'text': u'Mostly Cloudy', 'chance_precip': u'0', 'humidity': u'63', 'wind': {'gust': u'N/A', 'direction': u'93', 'speed': u'7', 'text': u'E'}, 'icon': u'27'}, 'date': u'Sep 25', 'day': {'brief_text': u'P Cloudy', 'text': u'Partly Cloudy', 'chance_precip': u'0', 'humidity': u'53', 'wind': {'gust': u'N/A', 'direction': u'94', 'speed': u'11', 'text': u'E'}, 'icon': u'30'}, 'sunrise': u'7:08 AM'}, {'day_of_week': u'Saturday', 'high': u'75', 'sunset': u'7:16 PM', 'low': u'56', 'night': {'brief_text': u'M Cloudy', 'text': u'Mostly Cloudy', 'chance_precip': u'20', 'humidity': u'65', 'wind': {'gust': u'N/A', 'direction': u'106', 'speed': u'8', 'text': u'ESE'}, 'icon': u'27'}, 'date': u'Sep 26', 'day': {'brief_text': u'P Cloudy', 'text': u'Partly Cloudy', 'chance_precip': u'10', 'humidity': u'51', 'wind': {'gust': u'N/A', 'direction': u'101', 'speed': u'10', 'text': u'E'}, 'icon': u'30'}, 'sunrise': u'7:08 AM'}, {'day_of_week': u'Sunday', 'high': u'75', 'sunset': u'7:16 PM', 'low': u'56', 'night': {'brief_text': u'Shwrs Early', 'text': u'Showers Early', 'chance_precip': u'60', 'humidity': u'83', 'wind': {'gust': u'N/A', 'direction': u'116', 'speed': u'8', 'text': u'ESE'}, 'icon': u'45'}, 'date': u'Sep 27', 'day': {'brief_text': u'PM Showers', 'text': u'PM Showers', 'chance_precip': u'60', 'humidity': u'66', 'wind': {'gust': u'N/A', 'direction': u'115', 'speed': u'11', 'text': u'ESE'}, 'icon': u'39'}, 'sunrise': u'7:08 AM'}]}
