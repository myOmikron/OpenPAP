from django.urls import path, include
from dashboard.views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('gamemaster/', include("gamemaster.urls")),
    path('player/', include("player.urls")),
]
