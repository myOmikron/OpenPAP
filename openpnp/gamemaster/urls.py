from django.urls import path, include
from gamemaster.views import *

urlpatterns = [
    path('', GameMasterView.as_view()),
    path('template/', include('template.urls')),
    path('campaign/', include('campaign.urls')),
    path('monster/', include('monster.urls')),
]
