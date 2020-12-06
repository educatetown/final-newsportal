from django.http import Http404
from django.shortcuts import render
from business.models import Business_News
from newsportalapp.models import News
from covid.models import Covid_News
from lifestyle.models import Lifestyle_News
from tech.models import Tech_News
from entertainment.models import Entertainment_News
from sports.models import Sports_News
from trending.models import Trending_News
from advertise.models import Advertising
from nepali_date import NepaliDate
from nepali.datetime import NepaliDate
from nepali.datetime import NepaliDateTime
from nepali.datetime import HumanizeDateTime

import datetime
# from nepali.datetime import NepaliDateTime
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


def all(request):
    news = News.objects.order_by('-published_at')
    business_news = Business_News.objects.order_by('-published_at')
    news_portal = News.objects.order_by('-published_at')
    covid_news = Covid_News.objects.order_by('-published_at')
    lifestyle_news = Lifestyle_News.objects.order_by('-published_at')
    tech_news = Tech_News.objects.order_by('-published_at')
    entertainment_news = Entertainment_News.objects.order_by('-published_at')
    sports_news = Sports_News.objects.order_by('-published_at')
    trending_news = Trending_News.objects.order_by('-published_at')
    advertise = Advertising.objects.order_by('-timestamp')
    nep_date = NepaliDate.today()
    now = datetime.datetime.now()

    context = {'news': news, 'business_news': business_news, 'news_portal': news_portal, 'covid_news': covid_news,
               'lifestyle_news': lifestyle_news, 'tech_news': tech_news, 'entertainment_news': entertainment_news,
               'sports_news': sports_news, 'trending_news': trending_news, 'advertise': advertise, 'nep_date': nep_date, 'now':now}

    template = 'newsportalapp/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        news = News.objects.get(slug=slug)
        advertise = Advertising.objects.order_by('-timestamp')
        all_news = News.objects.order_by('-published_at')[:4]
        news_pd = News.objects.get(slug=slug).published_at
        day = news_pd.day
        year = news_pd.year
        month = news_pd.month
        if len(str(month)) == 1:
            month = "0" + str(month)
            month = int(month)
        if len(str(day)) == 1:
            day = "0" + str(day)
            day = int(day)
        pub_date_ad = NepaliDate(year, month, day)
        np_date = NepaliDate.from_date(pub_date_ad)
        x = np_date.strftime('%A %d %B  %Y')

        context = {'news': news, 'advertise': advertise, 'all_news': all_news, 'x': x}
        template = 'newsportalapp/single.html'
        return render(request, template, context)

    except:
        raise Http404


class NewsCreateView(CreateView):
    model = News
    fields = '__all__'

