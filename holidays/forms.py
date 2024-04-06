from django import forms

class HolidayForms(forms.Form):
    Day = forms.IntegerField(label='Day', min_value=1, max_value=31)
    Month = forms.IntegerField(label='Month', min_value=1, max_value=12)
    Year = forms.IntegerField(label='Year', min_value=1900, max_value=2100)
    Country = forms.CharField(label='Country', max_length=2)
