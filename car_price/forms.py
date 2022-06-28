from django import forms

from car_price.models import CarPrice


class MarginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['margin'].empty_label = '1'

    class Meta:
        model = CarPrice
        fields = ('margin',)

