from django.shortcuts import render
from django.http import HttpResponse
from .forms import HolidayForms
import requests
import json

def holi_finder(request):
    forms = HolidayForms()
    if request.POST:
        data = request.POST.dict()
        request.session['your_data'] = data
        return redirect('holidays_result')
    return render(request, 'index.html', {'forms': forms})


def holidays_result(request):
    main_url = "https://holidays.abstractapi.com/v1/"
    your_api_key = ""
    data = request.session['your_data']
    your_country = data['Country']
    your_year = data['Year']
    your_month = data['Month']
    your_day = data['Day']

    full_url = "{url}?{api_key}&{country}&{year}&{month}&{day}".format(
            url=main_url,
            api_key=your_api_key,
            country=your_country,
            year=your_year,
            month=your_month,
            day=your_day
            )

    response = requests.get(full_url)
    api_response = response.json
    the_holiday = api_response['name']
    final_resp = "Today, {day}{month}{year}, is the holiday {holiday} in {country}.".format(
            day=your_day,
            month=your_month,
            year=your_year,
            holiday=the_holiday,
            country=your_country
            )

    return HttpResponse(final_resp)
