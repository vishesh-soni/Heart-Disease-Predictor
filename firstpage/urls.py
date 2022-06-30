from . import views
from django.urls import  path

urlpatterns = [
    path('',views.predict),
    path('output',views.output),
]