from django.http import Http404
from django.shortcuts import render
from .models import Trending_News
from advertise.models import Advertising
from nepali_date import NepaliDate
import datetime


def all(request):
    trending = Trending_News.objects.order_by('-published_at')
    advertise = Advertising.objects.order_by('-timestamp')
    nep_date = NepaliDate.today()
    now = datetime.datetime.now()

    context = {'trending': trending, 'advertise': advertise, 'nep_date': nep_date, 'now':now}
    template = 'trending/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        advertise = Advertising.objects.order_by('-timestamp')
        news = Trending_News.objects.get(slug=slug)
        nep_date = NepaliDate.today()
        now = datetime.datetime.now()

        all_news = Trending_News.objects.order_by('-published_at')[:4]

        context = {'news': news, 'advertise': advertise, 'all_news': all_news, 'nep_date': nep_date, 'now':now}
        template = 'trending/single.html'
        return render(request, template, context)

    except:
        raise Http404

