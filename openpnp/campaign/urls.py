from django.urls import path, include
from campaign.views import *

urlpatterns = [
    path('', CampaignView.as_view()),
]
