from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "dashboard/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"dashboard_link_player": "/player",
                                                    "dashboard_link_game_master": "/gamemaster",
                                                    "dashboard_link_settings": "/admin",
                                                    "breadcrumps": "Dashboard: Overwiew"})
