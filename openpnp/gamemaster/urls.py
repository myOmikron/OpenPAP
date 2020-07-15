from django.urls import path, include
from gamemaster.views import *

urlpatterns = [
    path('', GameMasterView.as_view()),
    path('template/', include('template.urls')),
]
