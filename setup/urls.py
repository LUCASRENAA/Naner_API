from django.contrib import admin
from django.urls import path,include
from naner.views import NotaViewSet, JogoViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('milhares', NotaViewSet, basename='Milhar_Jogo')
router.register('jogos', JogoViewSet, basename='Jogos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
]
