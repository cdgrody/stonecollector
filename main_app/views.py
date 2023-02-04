from django.shortcuts import render

stones = [
  {'name': 'Power Stone', 'color': 'Purple', 'ability': 'Grants the user immense physical strength and energy projection'},
  {'name': 'Reality Stone', 'color': 'Red', 'ability': 'Allows the user to manipulate reality and change physical laws'},
  {'name': 'Space Stone', 'color': 'Blue', 'ability': 'Allows the user to manipulate space and teleport to other locations'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def stones_index(request):
    return render(request, 'stones/index.html', {
        'stones': stones
    })