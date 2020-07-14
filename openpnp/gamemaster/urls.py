from django.urls import path
from gamemaster.views import *

urlpatterns = [
    path('', GameMasterView.as_view()),
    path('template', TemplatesView.as_view()),
    path('template/<pk>', UpdateTemplateView.as_view()),
    path('create_template', CreateTemplateView.as_view()),
]
