from django.shortcuts import render
from core.models import *

def home(request):
    services = Service.objects.all()
    promo_video = Promo_video.objects.first()
    pricings = Pricing.objects.all()
    context = {
        'services': services,
        'promo_video': promo_video,
        'pricings': pricings,
    }
    return render(request, 'index.html', context)
