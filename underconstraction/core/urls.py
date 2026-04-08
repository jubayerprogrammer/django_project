from django.urls import path
from core.views import account,home,contact

urlpatterns = [
    path("",home,name="home"),
    path("ac/",account,name="ac"),
    path("con/",contact,name="con")

    
]
