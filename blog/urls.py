from django.urls import path
from . import views
urlpatterns = [
   path('list', views.PostlistviewApi.as_view()),
   path('detail/<int:pk>', views.detailpostviewApi.as_view()),
   path('add', views.addpostApi.as_view())
]