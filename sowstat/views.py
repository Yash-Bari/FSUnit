from django.shortcuts import render, redirect
from .models import Crop
from django.db.models import Count

def index(request):
    crops = Crop.objects.all()
    return render(request, 'index.html', {'crops': crops})

def add_crop(request):
    if request.method == 'POST':
        name = request.POST['name']
        state = request.POST['state']
        sowing_date = request.POST['sowing_date']
        area = request.POST['area']
        crop = Crop(name=name, state=state, sowing_date=sowing_date, area=area)
        crop.save()
        return redirect('index')
    else:
        return render(request, 'add_crop.html')

def crop_detail(request, crop_id):
    crop = Crop.objects.get(id=crop_id)
    return render(request, 'crop_detail.html', {'crop': crop})


def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'crop_list.html', {'crops': crops})


def crop_statistics(request):
    crop_stats = Crop.objects.values('state', 'name').annotate(crop_count=Count('name'))
    crop_data = {}
    for crop_stat in crop_stats:
        state = crop_stat['state']
        name = crop_stat['name']
        crop_count = crop_stat['crop_count']
        if state not in crop_data:
            crop_data[state] = {}
        crop_data[state][name] = crop_count
    return render(request, 'crop_statistics.html', {'crop_data': crop_data})
