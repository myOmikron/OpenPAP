from django.shortcuts import render
from django.views.generic import TemplateView
from player.models import *


class PlayerView(TemplateView):
    template_name = "dashboard/player.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {"title": "OpenPnP - Player",
                                                    "dashboard_link_play": "/play",
                                                    "dashboard_link_character": "/character"})
