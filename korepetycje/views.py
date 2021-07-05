from django.shortcuts import render
from .forms import Search
from .models import Subject, Profile, Post
from django.views.generic import ListView,View
from django.http import HttpResponse
from hitcount.views import HitCountDetailView
from django.views.generic.detail import DetailView
import pandas as pd
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
    df = None
    tab = []


    form = Search(response.POST or None)
    if response.method == "POST":
        n = response.POST.get('subject')
        a = Subject.objects.filter(name = n).first()



        qs = Profile.objects.filter(subject = a)
        for query in qs:
            tab.append(query.subject)
        df = pd.DataFrame(qs.values())
        df['Subject'] = tab
        df = df.drop(columns=["id","user_id"])

        df = df.to_html()

        print(df)


    indeks = {"form":form, "df":df}
    return render(response,'Strglowna.html',indeks)

class CreateListProfile(ListView):
    model = Profile
    template_name = 'list.html'
    def get(self,response,*args,**kwargs):
        form = Search(re)


class Count(HitCountDetailView):
    model = Post
    template_name = "Strglowna.html"
    count_hit = True
    # slug_field = "slug"

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "Detail.html"






