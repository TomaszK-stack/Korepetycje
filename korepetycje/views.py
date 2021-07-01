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
        print(Subject.objects.get(name=a))
    tab = ['sdasd',4]
    ls = Profile.objects.all()
    index = {
        "form":form,
        "tab":tab,
        "ls":ls,
        }

    class CreateListProfile(ListView):
        model = Profile
        template_name = 'tomek.html'


    return render(response, "tomek.html", index)


class CreateListProfile(ListView):
    model = Profile
    template_name = 'tomek.html'
    # def get(self,response,*args,**kwargs):
    #     return HttpResponse("Hello world")
    def get(self,response,*args,**kwargs):
        ls = Profile.objects.all()
        form = Search(response.POST or None)
        indeks = {
            "ls":ls,
            "form":form,

        }


        return render(response,'tomek.html',indeks)



    # def post(self,response,*args,**kwargs):
    #
    #     return HttpResponse("Hello worldfsdfsdf")


def new(response):
    return render(response,'tomek.html',{})
