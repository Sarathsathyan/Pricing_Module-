from django.shortcuts import render
# 3rd party imports
from rest_framework import serializers, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import BasePriceSerializer
from .models import BasePrice
# Create your views here.

class BasePriceViewSet(viewsets.ModelViewSet):
    serializer_class = BasePriceSerializer
    queryset = BasePrice.objects.all()
    permission_classes = [AllowAny,]

    @action(methods=['post'], detail=True)
    def price_calculate(self, request, pk=None):
        """
            Calculate price based on the distance
            :param
                distance
        """
        data = request.data
        context = {}
        try:
            baseInfo = BasePrice.objects.get(id=pk)
        except BasePrice.DoesNotExist as e:
            raise serializers.ValidationError(
                "No Base price is set for the ride")

        distance = data.get('distance', None)

        if distance:
            price = (baseInfo.dbp + (distance * baseInfo.dap or 0)) * baseInfo.tbp or 0
            context["Total Price"] = price
            context["Base Price"] = baseInfo.dbp
            context["Distance Travelled"] = distance
            return Response(context, status=status.HTTP_200_OK)
        else:
            raise serializers.ValidationError(
                "Provide the distance")
