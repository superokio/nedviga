from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    form = BaseForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        dom = House.objects.create(
            type=request.POST.get('type'),
            title=request.POST.get('title'),
            bio=request.POST.get('bio'),
            address=request.POST.get('address'),
            price=request.POST.get('price'),
            size=request.POST.get('size'),
            material=request.POST.get('material'),
            rooms=request.POST.get('rooms'),
            furniture=request.POST.get('furniture'),
            repair=request.POST.get('repair'),
            near=request.POST.get('near'),
            date_of_building=request.POST.get('date_of_building'),
        )
        if dom.type == 'квартира':
            return redirect('nedviga:create_apartment', dom.pk)
        if dom.type == 'дом':
            return redirect('nedviga:create_house', dom.pk)
    return render(request, 'create.html', {'form': form, })


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
