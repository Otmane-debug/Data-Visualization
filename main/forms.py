from cProfile import label
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class AddData(forms.Form):
    value = forms.IntegerField(label="Indicateur", required=True)
    date = forms.DateField(widget=DateInput)
    
class RangeData(forms.Form):
    data_start = forms.DateField(label="Date Start ", widget=DateInput)
    data_end = forms.DateField(label="Date End ", widget=DateInput)