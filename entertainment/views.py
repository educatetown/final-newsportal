from django.http import Http404
from django.shortcuts import render
from .models import Entertainment_News
from advertise.models import Advertising
from nepali_date import NepaliDate
import datetime

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


def all(request):
    news = Entertainment_News.objects.order_by('-published_at')
    advertise = Advertising.objects.order_by('-timestamp')
    nep_date = NepaliDate.today()
    now = datetime.datetime.now()

    context = {'news': news, 'advertise': advertise, 'nep_date': nep_date, 'now':now}
    template = 'entertainment/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        news = Entertainment_News.objects.get(slug=slug)
        advertise = Advertising.objects.order_by('-timestamp')
        all_news = Entertainment_News.objects.order_by('-published_at')[:4]
        nep_date = NepaliDate.today()
        now = datetime.datetime.now()

        context = {'news': news, 'advertise': advertise, 'all_news': all_news, 'nep_date': nep_date, 'now':now}
        template = 'entertainment/single.html'
        return render(request, template, context)

    except:
        raise Http404


class NewsCreateView(CreateView):
    model = Entertainment_News
    fields = '__all__'

