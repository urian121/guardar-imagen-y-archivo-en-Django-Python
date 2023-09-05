from django.shortcuts import render, redirect

# from .forms import *
from .forms import SubirDumentoImagenForm
from .models import SubirDumentoImagen


def homepage(request):
    form = SubirDumentoImagenForm()
    return render(request, 'index.html', {'form': form})


def upload(request):
    if request.method == "POST":
        form = SubirDumentoImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("homepage")
    form = SubirDumentoImagenForm()
    movies = SubirDumentoImagen.objects.all()
    return render(request=request, template_name="index.html", context={'form': form, 'movies': movies})
