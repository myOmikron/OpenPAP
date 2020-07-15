from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView

from template.models import TemplateModel


class TemplatesView(TemplateView):
    template_name = "template/template.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"dashboard_link_create_template": "create",
                                                    "templates": [x for x in TemplateModel.objects.all()],
                                                    "breadcrumps": "Dashboard: Gamemaster: Template"})

    def post(self, request):
        print(request.POST.__dict__)
        return render(request, self.template_name, {"dashboard_link_create_template": "create",
                                                    "templates": [x for x in TemplateModel.objects.all()],
                                                    "breadcrumps": "Dashboard: Gamemaster: Template"})


class CreateTemplateView(CreateView):
    template_name = "template/create.html"
    model = TemplateModel
    fields = ["name", "skills", "attributes"]
    success_url = "/gamemaster/template/"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["breadcrumps"] = "Dashboard: Gamemaster: Template: Create Template"
        return ctx


class UpdateTemplateView(UpdateView):
    template_name = "template/update.html"
    model = TemplateModel
    fields = ["name", "skills", "attributes"]
    success_url = "/gamemaster/template/"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["breadcrumps"] = "Dashboard: Gamemaster: Template: Edit Template"
        return ctx
