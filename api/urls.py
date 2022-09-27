# Django imports
from django.urls import path, include
from .views import BasePriceViewSet
# 3rd party imports
from rest_framework import routers
router = routers.SimpleRouter()

router.register(r'price_info', BasePriceViewSet, 'set_price')

urlpatterns = [
    path('', include(router.urls)),

]
