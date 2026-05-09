from django.urls import path
from core.views import home,candidate

urlpatterns = [
    path("",home,name="home"),
    path("candidate/<int:pk>",candidate,name="candidate"),
]
  