from django import forms
from .models import *


class BaseForm(forms.ModelForm):
    type = forms.Select(choices=Type_choise, attrs={'class': 'dropdown'})
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    bio = forms.TextInput()
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input has-text-centered'}))
    size = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input has-text-centered'}))
    material = forms.ChoiceField(choices=Material_choise)
    rooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input has-text-centered', 'maxlength': '3',
                                                                          'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength)'}))
    furniture = forms.ChoiceField(choices=Furniture)
    repair = forms.ChoiceField(choices=Repair)
    near = forms.TextInput()
    date_of_building = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input has-text-centered', 'maxlength': '4',
                                                                          'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength)'}))

    class Meta:
        model = House
        fields = [
            'type', 'title', 'bio', 'address',
            'price',
            'size', 'material', 'rooms', 'furniture', 'repair',
            'near', 'date_of_building', ]


class ApartamentForm(forms.ModelForm):
    floor = forms.IntegerField(widget=forms.NumberInput)
    storeys = forms.IntegerField(widget=forms.NumberInput)
    building_type = forms.ChoiceField(choices=Building_type)

    class Meta:
        model = House
        fields = ['floor', 'storeys', 'building_type']


class HouseForm(forms.ModelForm):
    living_space = forms.IntegerField(widget=forms.NumberInput)
    location = forms.ChoiceField(choices=Location)
    convenience = forms.TextInput()

    class Meta:
        model = House
        fields = ['living_space', 'location', 'convenience']


class CustomFileField(forms.FileInput):
    pass


class ImageForm(forms.ModelForm):
    image1 = forms.ImageField(widget=CustomFileField(attrs={'class': 'input'}))
    image2 = forms.ImageField()
    image3 = forms.ImageField()
    image4 = forms.ImageField()
    image5 = forms.ImageField()
    image6 = forms.ImageField()
    image7 = forms.ImageField()
    image8 = forms.ImageField()
    image9 = forms.ImageField()
    image10 = forms.ImageField()
    image11 = forms.ImageField()
    image12 = forms.ImageField()
    image13 = forms.ImageField()
    image14 = forms.ImageField()
    image15 = forms.ImageField()
    image16 = forms.ImageField()

    class Meta:
        model = Image
        fields = ['image1', 'image2', 'image3', 'image4', 'image5', 'image6',
                  'image7','image8','image9','image10','image11','image12','image13','image14','image15','image16',]