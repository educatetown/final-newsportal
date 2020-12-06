from django.shortcuts import render
from django.views.generic import View, TemplateView
from business.models import Business_News
from covid.models import Covid_News
from entertainment.models import Entertainment_News
from lifestyle.models import Lifestyle_News
from sports.models import Sports_News
from tech.models import Tech_News
from trending.models import Trending_News
from django.db.models import Q


class Team(TemplateView):
    template_name = 'team.html'


class Advertising(TemplateView):
    template_name = 'advertising.html'


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        business = Business_News.objects.filter(
            Q(headline__icontains=q, ) |
            Q(description__icontains=q) |
            Q(reporter__icontains=q)
        )
        covid = Covid_News.objects.filter(headline__icontains=q)
        entertainment = Entertainment_News.objects.filter(headline__icontains=q)
        lifestyle = Lifestyle_News.objects.filter(headline__icontains=q)
        sports = Sports_News.objects.filter(headline__icontains=q)
        tech = Tech_News.objects.filter(headline__icontains=q)
        trend = Trending_News.objects.filter(headline__icontains=q)
        context = {'query': q, 'business': business, 'covid': covid, 'entertainment': entertainment, 'lifestyle': lifestyle,
                   'sports': sports, 'tech': tech, 'trend': trend}

        template = 'result.html'
    else:
        template = 'newsportalapp/all.html'
        context = {}
    return render(request, template, context)


