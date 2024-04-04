from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def holidays_result(request):
    main_url = "https://holidays.abstractapi.com/v1/"
    your_api_key = ""
    your_country = ""
    your_year = ""
    your_month = ""
    your_day = ""

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
    final_resp = "Today, {day}{month}{year}, is the holiday {holiday} in {country}.".format(
            day='',
            month='',
            year='',
            holiday='',
            country=''
            )

    return HttpResponse(final_resp)
