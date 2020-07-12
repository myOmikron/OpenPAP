from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from gamemaster.models import *
from gamemaster.forms import *


class GameMasterView(TemplateView):
    template_name = "dashboard/gamemaster.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "OpenPnP - GameMaster",
                                                    "dashboard_link_play": "play_gamemaster",
                                                    "dashboard_link_campaign": "campaign",
                                                    "dashboard_link_map": "map",
                                                    "dashboard_link_monster": "monster",
                                                    "dashboard_link_encounter": "encounter",
                                                    "dashboard_link_npc": "npc",
                                                    "dashboard_link_world_setting": "world_setting",
                                                    "dashboard_link_template": "template"})


class TemplatesView(TemplateView):
    template_name = "dashboard/template.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "OpenPnP - Templates",
                                                    "dashboard_link_create_template": "create_template",
                                                    "templates": [x for x in Template.objects.all()]})

    def post(self, request):
        print(request.POST.__dict__)
        return render(request, self.template_name, {"title": "OpenPnp - Templates",
                                                    "dashboard_link_create_template": "create_template",
                                                    "templates": [x for x in Template.objects.all()]})


class CreateTemplateView(FormView):
    template_name = "dashboard/create_template.html"
    form_class = CreateTemplateForm
    success_url = "template"

    def form_valid(self, form):
        form.create_template()
        return super().form_valid(form)
