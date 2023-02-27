from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    houses = House.objects.all()
    return render(request, 'home.html', {'houses': houses})


def create(request):
    form = BaseForm(request.POST, request.FILES)
    imagef = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            dom = House.objects.create(**form.cleaned_data)
            if imagef.is_valid():
                a = imagef.save(commit=False)
                a.house = dom
                a.save()
        if dom.type == 'квартира':
            return redirect('nedviga:create_apartment', dom.pk)
        if dom.type == 'дом':
            return redirect('nedviga:create_house', dom.pk)
    return render(request, 'create.html', {'form': form, 'form2': imagef})


def create_apartment(request, pk):
    house = House.objects.get(pk=pk)
    form = ApartamentForm(request.POST, instance=house)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('nedviga:home')
    return render(request, 'create_apartament.html', {'form': form})


def create_house(request, pk):
    house = House.objects.get(pk=pk)
    form = HouseForm(request.POST, instance=house)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('nedviga:home')
    return render(request, 'create_house.html', {'form': form})


def detail(request, pk):
    house = House.objects.get(pk=pk)
    return render(request, 'detail.html', {'house': house})
