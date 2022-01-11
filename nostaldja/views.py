from django.db.models.fields import FloatField
from django.shortcuts import render, redirect

from .models import Decade, Fad
from .forms import DecadeForm, FadForm

# view all decades
def decade_list(request): 
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})

# view decade details
def decade_detail(request, pk):
    decades = Decade.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decades':decades})

# create decade
def decade_create(request):
    if request.method == "POST":
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
        else:
            form = DecadeForm()
        return render(request, 'nostaldja/decade_form.html', {'form': form})

# edit decade
def decade_edit(request, pk):
    decade = Decade.objects.get(id = pk)
    if request.method == "POST":
        form = DecadeForm(request.POST, instance = decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance = decade)
    return render(request, 'nostaldja/decade_form.html')

# delete decade
def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decades')

# view all fads
def fad_list(request): 
    fads = Fad.objects.all()
    return render(request, 'nostaldja/fad.html', {'fads': fads})

# view fad details
def fad_detail(request, pk):
    fads = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html', {'fads':fads})

# create fad
def fad_create(request):
    if request.method == "POST":
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save()
            return redirect('fad_detail', pk=fad.pk)
        else:
            form = FadForm()
        return render(request, 'nostaldja/fad_form.html', {'form': form})

# edit fad
def fad_edit(request, pk):
    fad = Fad.objects.get(id = pk)
    if request.method == "POST":
        form = FadForm(request.POST, instance = fad)
        if form.is_valid():
            FloatField = form.save()
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm(instance = fad)
    return render(request, 'nostaldja/fad_form.html')

# delete fad
def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fads')

