from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from cocktails.models import Cocktail
from cocktails.models import Video


@login_required
def cocktails(
        request, *args, **kwargs
):
    if request.method == "GET":
        context = {
            "cocktails": Cocktail.objects.all()
        }
        return render(request, "cocktails.html", context=context)


@login_required
def recipes(
        request, *args, **kwargs
):
    if request.method == "GET":
        context = {
            "cocktails": Cocktail.objects.all()
        }
        return render(request, "recipes.html", context=context)


@login_required
def videos(
        request, *args, **kwargs
):
    if request.method == "GET":
        context = {
            "cocktails": Cocktail.objects.all(),
            "videos": Video.objects.all()
        }
        return render(request, "videos.html", context=context)


@login_required
def index(request):
    return render(request, 'home.html')


