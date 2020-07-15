from django.shortcuts import render
from django.views.generic import TemplateView


class MonsterView(TemplateView):
    template_name = "monster/monster.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"breadcrumps": "Dashboard: Gamemaster: Monsters: Overview",
                                                    "link_create_monster": "create"})
