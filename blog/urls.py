from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello_world),
    path('c', views.Cbv.as_view()),
]