from django.shortcuts import render
from core.models import *

def home(request):
    services = Service.objects.all()
    promo_video = Promo_video.objects.first()
    pricings = Pricing.objects.all()
    team = Team_member.objects.all()
    all_portfolios = Portfolio.objects.order_by('-id')
    branding_portfolios = Portfolio.objects.filter(category__name='BRANDING')
    marketing_portfolios = Portfolio.objects.filter(category__name='MARKETING')
    planning_portfolios = Portfolio.objects.filter(category__name='PLANNING')
    research_portfolios = Portfolio.objects.filter(category__name='RESEARCH')
    context = {
        'services': services,
        'promo_video': promo_video,
        'pricings': pricings,
        'team': team,
        'all_portfolios': all_portfolios,
        'branding_portfolios': branding_portfolios,
        'marketing_portfolios': marketing_portfolios,
        'planning_portfolios': planning_portfolios,
        'research_portfolios': research_portfolios,
    }
    return render(request, 'index.html', context)
