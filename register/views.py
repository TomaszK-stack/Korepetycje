from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import Register
# Create your views here
def register(response):
    if response.method == "POST":
        form = Register(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = Register()
    return render(response,'register.html',{"form":form})
