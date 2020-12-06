from django.http import Http404
from django.shortcuts import render
from .models import Covid_News
from advertise.models import Advertising
from nepali_date import NepaliDate
import datetime

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


def all(request):
    covid_news = Covid_News.objects.all()
    advertise = Advertising.objects.order_by('-timestamp')
    nep_date = NepaliDate.today()
    now = datetime.datetime.now()

    context = {'covid_news': covid_news, 'advertise': advertise, 'nep_date': nep_date, 'now':now}
    template = 'covid/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        news = Covid_News.objects.get(slug=slug)
        all_news = Covid_News.objects.order_by('-published_at')[:4]
        advertise = Advertising.objects.order_by('-timestamp')
        nep_date = NepaliDate.today()
        now = datetime.datetime.now()

        context = {'news': news, 'advertise': advertise, 'all_news':all_news, 'nep_date': nep_date, 'now':now}
        template = 'covid/single.html'
        return render(request, template, context)

    except:
        raise Http404


class NewsCreateView(CreateView):
    model = Covid_News
    fields = '__all__'

