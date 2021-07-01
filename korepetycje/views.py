from django.shortcuts import render
from .forms import Search
from .models import Subject, Profile
from django.views.generic import ListView,View
from django.http import HttpResponse
# Create your views here.

def base(response):
    form = Search(response.POST or None)
    if response.method == "POST":
        a = response.POST.get('name')
        print(Profile.objects.get(name=a))
    tab = ['sdasd',4]
    ls = Profile.objects.all()
    index = {
        "form":form,
        "tab":tab,
        "ls":ls,
        }




    return render(response, "Strglowna.html", index)


class CreateListProfile(ListView):
    model = Profile
    template_name = 'Strglowna.html'


    def get(self,response,*args,**kwargs):
        ls = Profile.objects.all()
        form = Search(response.POST or None)

        indeks = {
            "ls":ls,
            "form":form,

        }
        return render(response,'Strglowna.html',indeks)













def new(response):
    ls = Profile.objects.all()
    tab = []
    form = Search(response.POST or None)
    sub = ''
    if response.method == "POST":
        sub = response.POST.get('subject')

        # for z in ls:
        #     if z.subject == sub:
        #         tab.append(z)


    indeks = {"form":form, "tab":tab, "sub":sub, "ls": ls}
    return render(response,'Strglowna.html',indeks)

class CreateListProfile(ListView):
    model = Profile
    template_name = 'list.html'


