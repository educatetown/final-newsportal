from django.http import Http404
from django.shortcuts import render
from .models import Itself_News
from business.models import Business_News
from newsportalapp.models import News
from covid.models import Covid_News
from lifestyle.models import Lifestyle_News
from tech.models import Tech_News
from entertainment.models import Entertainment_News
from sports.models import Sports_News
from advertise.models import Advertising
from nepali_date import NepaliDate
import datetime

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


def all(request):
    business_news = Business_News.objects.order_by('-published_at')
    news_portal = News.objects.order_by('-published_at')
    news = Itself_News.objects.order_by('-published_at')
    covid_news = Covid_News.objects.order_by('-published_at')
    lifestyle_news = Lifestyle_News.objects.order_by('-published_at')
    tech_news = Tech_News.objects.order_by('-published_at')
    entertainment_news = Entertainment_News.objects.order_by('-published_at')
    sports_news = Sports_News.objects.order_by('-published_at')
    advertise = Advertising.objects.order_by('-timestamp')
    nep_date = NepaliDate.today()
    now = datetime.datetime.now()

    context = {'news': news, 'business_news': business_news, 'news_portal': news_portal, 'covid_news': covid_news, 'lifestyle_news':lifestyle_news, 'tech_news':tech_news, 'entertainment_news':entertainment_news, 'sports_news': sports_news, 'advertise': advertise, 'nep_date': nep_date, 'now':now}
    template = 'news/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        news = Itself_News.objects.get(slug=slug)
        advertise = Advertising.objects.order_by('-timestamp')
        nep_date = NepaliDate.today()
        now = datetime.datetime.now()

        all_news = Covid_News.objects.order_by('-published_at')[:4]

        context = {'news': news, 'advertise': advertise, 'all_news':all_news, 'nep_date': nep_date, 'now':now}
        template = 'news/single.html'
        return render(request, template, context)

    except:
        raise Http404


class NewsCreateView(CreateView):
    model = Itself_News
    fields = '__all__'

