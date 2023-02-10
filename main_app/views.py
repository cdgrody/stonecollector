from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import Stone, Movie
from .forms import WeilderForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def stones_index(request):
    stones = Stone.objects.all()
    return render(request, 'stones/index.html', {
        'stones': stones
    })

def stones_detail(request, stone_id):
    stone = Stone.objects.get(id=stone_id)
    id_list = stone.movies.all().values_list('id')
    movies_stone_doesnt_have = Movie.objects.exclude(id__in=id_list)
    weilder_form = WeilderForm()
    return render(request, 'stones/detail.html', {
        'stone': stone, 
        'weilder_form': weilder_form,
        'movies': movies_stone_doesnt_have
    })

class StoneCreate(CreateView):
    model = Stone
    fields = '__all__'

class StoneUpdate(UpdateView):
    model = Stone
    fields = ['color', 'numberOfAppearances', 'description']

class StoneDelete(DeleteView):
    model = Stone
    success_url = '/movies'


def add_weilder(request, stone_id):
    form = WeilderForm(request.POST)
    if form.is_valid():
        new_weilder = form.save(commit=False)
        new_weilder.stone_id = stone_id
        new_weilder.save()
    return redirect('detail', stone_id=stone_id)


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['release_date', 'is_ensemble']


class MovieDelete(DeleteView):
    model = Movie
    success_url = '/stones'


class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'


def assoc_movie(request, stone_id, movie_id):
    print('stone id here', stone_id)
    Stone.objects.get(id=stone_id).movies.add(movie_id)
    return redirect('detail', stone_id=stone_id)

def unassoc_movie(request, stone_id, movie_id):
    print('stone id here', stone_id)
    Stone.objects.get(id=stone_id).movies.remove(movie_id)
    return redirect('detail', stone_id=stone_id)