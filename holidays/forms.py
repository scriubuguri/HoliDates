from django import forms

class HolidayForms(forms.Form):
    day = forms.IntegerField(label='Day', min_value=1, max_value=31)
    month = forms.IntegerField(label='Month', min_value=1, max_value=12)
    year = forms.IntegerField(label='Year', min_value=1900, max_value=2100)
    country = forms.CharField(label='Country', max_length=2)
