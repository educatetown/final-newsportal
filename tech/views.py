from django.http import Http404
from django.shortcuts import render
from .models import Tech_News
from advertise.models import Advertising
from nepali_date import NepaliDate
import datetime

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


def all(request):
    news = Tech_News.objects.order_by('-published_at')
    advertise = Advertising.objects.order_by('-timestamp')
    nep_date = NepaliDate.today()
    now = datetime.datetime.now()
    context = {'news': news, 'advertise': advertise, 'nep_date': nep_date, 'now':now}
    template = 'tech/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        news = Tech_News.objects.get(slug=slug)
        advertise = Advertising.objects.order_by('-timestamp')
        nep_date = NepaliDate.today()
        now = datetime.datetime.now()

        all_news = Tech_News.objects.order_by('-published_at')[:4]

        context = {'news': news, 'advertise': advertise, 'all_news': all_news, 'nep_date': nep_date, 'now':now}
        template = 'tech/single.html'
        return render(request, template, context)

    except:
        raise Http404


class NewsCreateView(CreateView):
    model = Tech_News
    fields = '__all__'

