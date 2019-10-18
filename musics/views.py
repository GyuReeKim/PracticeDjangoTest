from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicForm, FavorForm
from .models import Music, Favor

# Create your views here.
def index(request):
    musics = Music.objects.all()
    context = {
        'musics': musics,
    }
    return render(request, 'musics/index.html', context)

def create(request):
    if request.method == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musics:index')
    else:
        form = MusicForm()
    context = {
        'form': form,
    }
    return render(request, 'musics/form.html', context)

def detail(request, id):
    music = get_object_or_404(Music, id=id)
    form = FavorForm()
    favors = music.favor_set.all()
    favor_1 = favors.filter(pick=1).count()
    favor_2 = favors.filter(pick=2).count()
    total = favor_1 + favor_2
    favor_per_1 = round(favor_1 / total * 100)
    favor_per_2 = round(favor_2 / total * 100)
    context = {
        'music': music,
        'form': form,
        'favor_per_1': favor_per_1,
        'favor_per_2': favor_per_2,
    }
    return render(request, 'musics/detail.html', context)

def update(request, id):
    music = get_object_or_404(Music, id=id)
    if request.method == "POST":
        form = MusicForm(request.POST, instance=music)
        if form.is_valid():
            form.save()
            return redirect('musics:detail', id)
    else:
        form = MusicForm(instance=music)
    context = {
        'music': music,
        'form': form,
    }
    return render(request, 'musics/form.html', context)

def delete(request, id):
    music = get_object_or_404(Music, id=id)
    if request.method == "POST":
        music.delete()
        return redirect('musics:index')

def favor_create(request, id):
    music = get_object_or_404(Music, id=id)
    if request.method == "POST":
        form = FavorForm(request.POST)
        if form.is_valid():
            favor = form.save(commit=False)
            favor.music = music
            favor.save()
            return redirect('musics:detail', id)

def favor_delete(request, music_id, favor_id):
    favor = get_object_or_404(Favor, id=favor_id)
    if request.method == "POST":
        favor.delete()
        return redirect('musics:detail', music_id)

