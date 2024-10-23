from django.shortcuts import render, redirect
from .forms import VideoGameForm
from .models import VideoGame

# Create your views here.


def videogame_list(request):
    context = {'videogame_list': VideoGame.objects.all()}
    return render(request, "videogames_register/videogame_list.html", context)


def videogame_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = VideoGameForm()
        else:
            videogame = VideoGame.objects.get(pk=id)
            form = VideoGameForm(instance=videogame)
        return render(request, "videogames_register/videogame_form.html", {'form': form})
    else:
        if id == 0:
            form = VideoGameForm(request.POST)
        else:
            videogame = VideoGame.objects.get(pk=id)
            form = VideoGameForm(request.POST,instance= videogame)
        if form.is_valid():
            form.save()
        return redirect('/videogame/list')



def videogame_delete(request,id):
    videogame = VideoGame.objects.get(pk=id)
    videogame.delete()
    return redirect('/videogame/list')