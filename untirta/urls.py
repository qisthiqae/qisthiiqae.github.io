import imp
from django.contrib import admin
from django.urls import path
from faperta.views import isifaperta
from feb.views import isifeb
from fh.views import isifh
from fisip.views import isifisip
from fk.views import isifk
from fkip.views import isifkip
from ft.views import isift
from pascasarjana.views import isipasca
from profil.views import isiprofil
from profil.views import isitentang
from profil.views import isilokasi
from untirta.views import isiuntirta
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', isifaperta),
    path('feb/', isifeb),
    path('fh/', isifh),
    path('fisip/', isifisip),
    path('fk/', isifk),
    path('fkip/', isifkip),
    path('ft/', isift),
    path('pascasarjana/', isipasca),
    path('profil/', isiprofil),
    path('untirta/', isiuntirta),
    path('tentang/', isitentang),
    path('lokasi/', isilokasi),
    path('', views.isiuntirta),
]
