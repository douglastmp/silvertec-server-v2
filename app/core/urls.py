from django.urls import path, include
from rest_framework import routers

from core import views

router = routers.SimpleRouter()
router.register('orders', views.OrderViewSet)
router.register('brands', views.BrandViewSet)
router.register('processors', views.ProcessorViewSet)
router.register('motherboards', views.MotherboardViewSet)
router.register('memories', views.MemoryViewSet)
router.register('graphic-cards', views.GraphicCardViewSet)


app_name = 'core'

urlpatterns = [
    path('', include(router.urls))
]
