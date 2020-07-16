from django.core import serializers
from django.http import JsonResponse
from django.views.generic import TemplateView

from monster.models import Monster


class ListMonster(TemplateView):
    def get(self, request, *args, **kwargs):
        try:
            data = {"success": True, "message": [{x.id: x.name} for x in Monster.objects.filter(tag__tag="monster")]}
        except:
            data = {"success": False, "message": "Something went wrong"}
        return JsonResponse(data, safe=False)


class GetMonster(TemplateView):
    def get(self, request, *args, **kwargs):
        if "id" not in request.GET:
            return JsonResponse({"success": False, "message": "No ID submitted"})
        data = {"success": True, "message": Monster.objects.get(id=request.GET["id"]).get_json()}
        return JsonResponse(data, safe=False)
