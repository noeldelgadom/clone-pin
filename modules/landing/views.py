from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as salir, login as iniciar
from django.http import HttpResponse
# Create your views here.

def index(request):

    return render(request, 'landing/index.html',{'request':request})



def login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                iniciar(request, user)
                return redirect('landing:index')
            else:
                return HttpResponse('Usuario no encontrado')
    return render(request, 'landing/login.html', {'log':form})


def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':

        print(form.is_valid())
        if form.is_valid():
            form.cleaned_data.pop('confirm_password', None)
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            return redirect("landing:index")

    return render(request,'landing/sign.html',{'sign':form})




def logout(request):
    salir(request)
    return redirect("landing:index")

def uploadImage(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid:
            image = form.save(commit=False)
            tags = form.cleaned_data['tags'].split(',')
            image.tags = tags
            image.save()
            return redirect('landing:index')
    else:
        form = ImageUploadForm()
        return render(request, 'landing/form_image.html',{'form': form})
