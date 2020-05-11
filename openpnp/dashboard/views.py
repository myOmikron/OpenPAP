from django.shortcuts import render
from django.views.generic import TemplateView


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
                                                    "dashboard_link_create_campaign": "/create_campaign",
                                                    "dashboard_link_create_map": "/create_map",
                                                    "dashboard_link_create_monster": "/create_monster",
                                                    "dashboard_link_create_encounter": "/create_encounter",
                                                    "dashboard_link_create_npc": "/create_npc",
                                                    "dashboard_link_create_world_setting": "/create_world_setting"})


class PlayerView(TemplateView):
    template_name = "dashboard/player.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "OpenPnP - Player",
                                                    "dashboard_link_play": "/play",
                                                    "dashboard_link_character": "/character"})
