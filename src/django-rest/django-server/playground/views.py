import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import datetime

from .models import GeeksModel
from .serializers import GeeksModelSerializer

import myserver

_services = myserver.ServiceFactory.get_instance()


# Create your views here
#

@api_view(['GET', 'POST', 'DELETE'])
def say_hello(request):
    return render(request, 'hello.html', {"name": "cool"})


@api_view(['GET', 'POST', 'DELETE'])
def report_time(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)


@api_view(['GET', 'POST', 'DELETE'])
def all_models(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()

    return render(request, "list_view.html", context)


@api_view(['GET', 'POST', 'DELETE'])
def model_list(request):
    models = GeeksModel.objects.all()
    serializer = GeeksModelSerializer(models, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def model_detail(request, pk):
    models = GeeksModel.objects.get(id=pk)
    serializer = GeeksModelSerializer(models, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def model_delete(request, pk):
    model = GeeksModel.objects.get(id=pk)
    model.delete()
    now = datetime.datetime.now()
    # convert to string
    html = "Model {} deleted at time {}".format(pk, now)
    # return response
    return HttpResponse(html)


@api_view(['GET', 'POST', 'DELETE'])
def add(request):
    if request.method == "POST":
        inputs = JSONParser().parse(request)
        print(inputs)
        result = _services.calculation_servicer.add(inputs["input"])
        return JsonResponse({"value": f"result = {result}"})
    elif request.method == "POST":
        raise NotImplementedError()
    elif request.method == "DELETE":
        raise NotImplementedError()
