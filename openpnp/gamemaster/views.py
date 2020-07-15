from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView
from gamemaster.models import *


class GameMasterView(TemplateView):
    template_name = "dashboard/gamemaster.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"dashboard_link_play": "play_gamemaster",
                                                    "dashboard_link_campaign": "campaign",
                                                    "dashboard_link_map": "map",
                                                    "dashboard_link_monster": "monster",
                                                    "dashboard_link_encounter": "encounter",
                                                    "dashboard_link_npc": "npc",
                                                    "dashboard_link_world_setting": "world_setting",
                                                    "dashboard_link_template": "template",
                                                    "breadcrumps": "Dashboard: Gamemaster: Overwiew"})
