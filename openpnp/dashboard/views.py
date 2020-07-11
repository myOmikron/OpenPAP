from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView

from dashboard import forms
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
                                                    "dashboard_link_create_template": "/create_template",
                                                    "templates": [x for x in Template.objects.all()]})

    def post(self, request):
        print(request.POST.__dict__)
        return render(request, self.template_name, {"title": "OpenPnp - Templates",
                                                    "dashboard_link_create_template": "/create_template",
                                                    "templates": [x for x in Template.objects.all()]})


class CreateTemplateView(FormView):
    template_name = "dashboard/create_template.html"
    form_class = forms.CreateTemplateForm
    success_url = "/template"

    def form_valid(self, form):
        form.create_template()
        return super().form_valid(form)


class PlayerView(TemplateView):
    template_name = "dashboard/player.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {"title": "OpenPnP - Player",
                                                    "dashboard_link_play": "/play",
                                                    "dashboard_link_character": "/character"})
