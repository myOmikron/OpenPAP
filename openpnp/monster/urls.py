from django.urls import path, include
from monster.views import *

urlpatterns = [
    path('', MonsterView.as_view()),
]
