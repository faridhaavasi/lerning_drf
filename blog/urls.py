from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('postapi', views.List_post_API.as_view()),
    path('postapi/<int:pk>', views.Detail_post_API.as_view()),
    path('addpost', views.addpost.as_view()),
    path('update/<int:pk>', views.updataApi.as_view()),
    path('delete/<int:pk>', views.deleteApi.as_view())
]