from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    houses = House.objects.all()
    return render(request, 'home.html', {'houses': houses})


@login_required(login_url='/auth/login')
def create(request):
    form = BaseForm(request.POST, request.FILES)
    image_form = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            dom = House.objects.create(user=request.user, **form.cleaned_data)
            if image_form.is_valid():
                a = image_form.save(commit=False)
                a.house = dom
                a.save()
        if dom.type == 'квартира':
            return redirect('house:create_apartment', dom.pk)
        if dom.type == 'дом':
            return redirect('house:create_house', dom.pk)
    return render(request, 'create.html', {'form': form, 'form2': image_form})


def create_apartment(request, pk):
    house = House.objects.get(pk=pk)
    form = ApartamentForm(request.POST, instance=house)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('house:home')
    return render(request, 'create_apartament.html', {'form': form})


def create_house(request, pk):
    house = House.objects.get(pk=pk)
    form = HouseForm(request.POST, instance=house)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('house:home')
    return render(request, 'create_house.html', {'form': form})


def detail(request, pk):
    house = House.objects.get(pk=pk)
    images = Image.objects.filter(house=house)
    return render(request, 'detail.html', {'house': house, 'images': images})
