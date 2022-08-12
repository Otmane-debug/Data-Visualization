from django.utils import timezone
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class AddData(forms.Form):
    value = forms.IntegerField(label="Indicateur", required=True)
    date = forms.DateField(widget=DateInput)
    
class RangeData(forms.Form):
    data_start = forms.DateField(widget=DateInput)
    data_end = forms.DateField(widget=DateInput)
    
class Add_Other_Data(forms.Form):
    value = forms.IntegerField(label="Value", required=True)