from django import forms
from .models import *


class BaseForm(forms.ModelForm):
    type = forms.ChoiceField(choices=Type_choise)
    title = forms.CharField(widget=forms.TextInput)
    bio = forms.TextInput()
    address = forms.CharField(widget=forms.TextInput)
    price = forms.IntegerField(widget=forms.NumberInput)
    size = forms.IntegerField(widget=forms.NumberInput)
    material = forms.ChoiceField(choices=Material_choise)
    rooms = forms.IntegerField(widget=forms.NumberInput)
    furniture = forms.ChoiceField(choices=Furniture)
    repair = forms.ChoiceField(choices=Repair)
    near = forms.TextInput()
    date_of_building = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = House
        fields = ['type', 'title', 'bio', 'address', 'price',
                  'size', 'material', 'rooms', 'furniture', 'repair',
                  'near', 'date_of_building']


class ApartamentForm(forms.ModelForm):
    floor = forms.IntegerField(widget=forms.NumberInput)
    storeys = forms.IntegerField(widget=forms.NumberInput)
    building_type = forms.ChoiceField(choices=Building_type)
    image = forms.ImageField()

    class Meta:
        model = House
        fields = ['floor', 'storeys', 'building_type', 'image']


class HouseForm(forms.ModelForm):
    living_space = forms.IntegerField(widget=forms.NumberInput)
    location = forms.ChoiceField(choices=Location)
    convenience = forms.TextInput()
    image = forms.ImageField()

    class Meta:
        model = House
        fields = ['living_space', 'location', 'convenience','image']
