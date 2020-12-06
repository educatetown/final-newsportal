from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render
from .models import Lifestyle_News
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from advertise.models import Advertising
from nepali_date import NepaliDate
import datetime

def all(request):
    news = Lifestyle_News.objects.order_by('-published_at')
    nep_date = NepaliDate.today()
    now = datetime.datetime.now()

    context = {'news': news, 'nep_date': nep_date, 'now':now}
    template = 'lifestyle/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        news = Lifestyle_News.objects.get(slug=slug)
        nep_date = NepaliDate.today()
        now = datetime.datetime.now()

        all_news = Lifestyle_News.objects.order_by('-published_at')[:4]
        advertise = Advertising.objects.order_by('-timestamp')

        context = {'news': news, 'advertise': advertise, 'all_news':all_news, 'nep_date': nep_date, 'now':now}
        template = 'lifestyle/single.html'
        return render(request, template, context)

    except:
        raise Http404


class NewsCreateView(CreateView):
    model = Lifestyle_News
    fields = '__all__'

