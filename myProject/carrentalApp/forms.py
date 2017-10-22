from django import forms

class carrentalForm(forms.Form):
    pick_up_date = forms.DateField(required=False)
    drop_off_date = forms.DateField(required=False)
    location = forms.CharField(required=False)
    currency = forms.CharField(required=False)
    language = forms.CharField(required=False)
