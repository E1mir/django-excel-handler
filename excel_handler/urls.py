from django.urls import path
from . import views

app_name = "excel_handled"

urlpatterns = [
    path('', views.HelloWorld.as_view(), name='index'),
    # path('hello/', views.HelloWorld.as_view(), name="hello")
]
