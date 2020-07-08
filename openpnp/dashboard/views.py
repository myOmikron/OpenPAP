from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from dashboard.models import *


class IndexView(TemplateView):
    template_name = "dashboard/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "OpenPnP - Dashboard",
                                                    "dashboard_link_player": "/player",
                                                    "dashboard_link_game_master": "/gamemaster",
                                                    "dashboard_link_settings": "/admin"})


class GameMasterView(TemplateView):
    template_name = "dashboard/gamemaster.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "OpenPnP - GameMaster",
                                                    "dashboard_link_play": "/play_gamemaster",
                                                    "dashboard_link_campaign": "/campaign",
                                                    "dashboard_link_map": "/map",
                                                    "dashboard_link_monster": "/monster",
                                                    "dashboard_link_encounter": "/encounter",
                                                    "dashboard_link_npc": "/npc",
                                                    "dashboard_link_world_setting": "/world_setting",
                                                    "dashboard_link_template": "/template"})


class TemplatesView(TemplateView):
    template_name = "dashboard/template.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "OpenPnP - Templates",
                                                    "dashboard_link_create_template": "/create_template"})


class CreateTemplateView(TemplateView):
    template_name = "dashboard/create_template.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request):
        return redirect('/template')


class PlayerView(TemplateView):
    template_name = "dashboard/player.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {"title": "OpenPnP - Player",
                                                    "dashboard_link_play": "/play",
                                                    "dashboard_link_character": "/character"})
