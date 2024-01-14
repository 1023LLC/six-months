from django.shortcuts import render
import json
import urllib.request

def index(request):
    data = {}
    
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '9dacc9f8b3471f2472fc847bd5f51142'
        
        try:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}'
            res = urllib.request.urlopen(url).read()
            json_data = json.loads(res)

            # Check if the API response contains the expected data
            if 'sys' in json_data and 'coord' in json_data and 'main' in json_data:
                data = {
                    "city": city,
                    "country_code": str(json_data['sys']['country']),
                    "coordinate": f"{json_data['coord']['lon']} {json_data['coord']['lat']}",
                    "temp": f"{json_data['main']['temp']}k",
                    "pressure": str(json_data['main']['pressure']),
                    "humidity": str(json_data['main']['humidity']),
                }
            else:
                data = {"error": "Invalid API response"}

        except urllib.error.HTTPError as e:
            data = {"error": f"HTTP Error {e.code}: {e.reason}"}
        except ValueError as e:
            data = {"error": f"JSON Parsing Error: {e}"}

    return render(request, 'weather/index.html', data)
