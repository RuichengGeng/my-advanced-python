from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response

from .models import Drinks
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def drink_list(request):
    # get all the drinks
    # serialize them and return json
    if request.method == "GET":
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT','DELETE'])
def drink_detail(request, id):
    try:
        res = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = DrinkSerializer(res)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = DrinkSerializer(res, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        res.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
