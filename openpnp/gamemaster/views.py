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


class TemplatesView(TemplateView):
    template_name = "dashboard/template.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"dashboard_link_create_template": "create_template",
                                                    "templates": [x for x in Template.objects.all()],
                                                    "breadcrumps": "Dashboard: Gamemaster: Template"})

    def post(self, request):
        print(request.POST.__dict__)
        return render(request, self.template_name, {"dashboard_link_create_template": "create_template",
                                                    "templates": [x for x in Template.objects.all()],
                                                    "breadcrumps": "Dashboard: Gamemaster: Template"})


class CreateTemplateView(CreateView):
    template_name = "dashboard/create_template.html"
    model = Template
    fields = ["name"]
    success_url = "template"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["breadcrumps"] = "Dashboard: Gamemaster: Template: CreateTemplate"
        return ctx


class UpdateTemplateView(UpdateView):
    template_name = "dashboard/update_template.html"
    model = Template
    fields = ["name"]
    success_url = "/gamemaster/template"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["breadcrumps"] = "Dashboard: Gamemaster: Template: Edit Template"
        return ctx
