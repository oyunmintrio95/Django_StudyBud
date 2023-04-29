from django.shortcuts import render
from .models import Room

# Create your views here.


rooms = [
    {'id': 1, 'name':'Lets learn python!'},
    {'id': 2, 'name':'Design with me'},
    {'id': 3, 'name':'Frontend developers'},
]
def home(request):
    # passing data to render to html
    # return render(request, 'home.html', {'rooms': rooms})
    # queryset = ModelName.objects.all()
    # Variable that holds response = Model Name. Model obejcts attrubute. methods
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)

    context = {'room' : room}
    return render(request, 'base/room.html', context)