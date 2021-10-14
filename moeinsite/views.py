from django.shortcuts import render , redirect
from .models import Info , Musics , MusicsInfo
from .forms import Message
from django.contrib import messages

# Create your views here.

def home(request):
    info = Info.objects.all()
    musics = Musics.objects.all()
    musicsinfo = MusicsInfo.objects.all()
    form = Message(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("congrat")
        else:
            messages.error(request , "SORRY , TRY AGAIN LATER!")

    return render(request , 'moeinsite/index.html' , context = {'info':info , 'musics':musics , 'musicsinfo':musicsinfo , "form" : form})
    

def congratulations(request):
    return render(request , 'moeinsite/congratulation.html')