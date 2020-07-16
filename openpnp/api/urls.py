from django.urls import path, include
from api.views import *

urlpatterns = [
    path('listMonster', ListMonster.as_view()),
    path('getMonster', GetMonster.as_view()),
]
