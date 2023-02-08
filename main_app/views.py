from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stone

# stones = [
#   {'name': 'Power Stone', 'color': 'Purple', 'ability': 'Grants the user immense physical strength and energy projection'},
#   {'name': 'Reality Stone', 'color': 'Red', 'ability': 'Allows the user to manipulate reality and change physical laws'},
#   {'name': 'Space Stone', 'color': 'Blue', 'ability': 'Allows the user to manipulate space and teleport to other locations'},
# ]

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
    return render(request, 'stones/detail.html', {'stone': stone})

class StoneCreate(CreateView):
    model = Stone
    fields = '__all__'

class StoneUpdate(UpdateView):
    model = Stone
    fields = ['color', 'numberOfAppearances', 'description']

class StoneDelete(DeleteView):
    model = Stone
    success_url = '/stones'