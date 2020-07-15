from django.urls import path
from template.views import *

urlpatterns = [
    path('', TemplatesView.as_view()),
    path('create', CreateTemplateView.as_view()),
    path('<pk>', UpdateTemplateView.as_view()),
]
