from django.shortcuts import render
from django.contrib.auth.models import User
from testapp.forms import TicketSignupForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from testapp.models import Location,Theatre
# Create your views here.

def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def login_view(request):
    return render(request,'registration/login.html')

def signup_view(request):
    form=TicketSignupForm()
    if request.method=='POST':
        form=TicketSignupForm(request.POST)
        if form.is_valid():
            User=form.save()
        User.set_password(User.password)
        User.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})

def movie_view(request):
    return render(request,'testapp/movie.html')

def location_view(request):
    locations=Location.objects.all()
    return render(request,'testapp/location.html',{'locations':locations})

def select_view(request,id):
    locations=Location.objects.get(id=id)
    return render(request,'testapp/movie.html',{'locations':locations})

def theatres_view(request):
    theatres=Theatre.objects.all()
    return render(request,'testapp/theatre.html',{'theatres':theatres})

def ticketing_view(request):
    return render(request,'testapp/tickets.html')

def thankyou_view(request):
    return render(request,'testapp/thankyou.html')
