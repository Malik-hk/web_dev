from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def hamza(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=abca19531437c4d7d07c9ae1b6fcaf5a').read()

        list_of_data = json.loads(source)
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '+ str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(list_of_data) 

    else:
        data={}
        print('Nothing to Show..')


    return render(request, 'web_app/home.html', data)
