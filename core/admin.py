from django.contrib import admin
from core.models import *

admin.site.register([
    Client,
    Promo_video,
    Service,
    Portfolio,
    Blog,
    Review,
    Pricing,
    Team_member,
    Contact,
    Category,])