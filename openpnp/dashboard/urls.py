from django.urls import path
from dashboard.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]