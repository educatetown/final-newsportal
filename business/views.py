from django.http import Http404
from django.shortcuts import render
from .models import Business_News
from advertise.models import Advertising
from nepali_date import NepaliDate
import datetime

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


def all(request):
    news = Business_News.objects.order_by('-published_at')
    advertise = Advertising.objects.order_by('-timestamp')
    nep_date = NepaliDate.today()
    now = datetime.datetime.now()

    context = {'news': news, 'advertise': advertise, 'nep_date': nep_date, 'now':now}
    template = 'business/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        news = Business_News.objects.get(slug=slug)
        all_news = Business_News.objects.order_by('-published_at')[:4]
        advertise = Advertising.objects.order_by('-timestamp')
        nep_date = NepaliDate.today()
        now = datetime.datetime.now()

        context = {'news': news, 'advertise': advertise, 'all_news':all_news, 'nep_date': nep_date, 'now':now}
        template = 'business/single.html'
        return render(request, template, context)

    except:
        raise Http404

