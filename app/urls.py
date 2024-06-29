from django.urls import path
from .views import HomePageView, DetailPageView, CreatePageView, UpdatePageview, DeletePageView


urlpatterns  =[
    path("",HomePageView.as_view(), name="home"),
    path('detail/<int:pk>/', DetailPageView.as_view(), name="detail"),
    path('create', CreatePageView.as_view(), name="create"),
    path("detail/<int:pk>/update", UpdatePageview.as_view(), name="update"),
    path("detail/<int:pk>/delete", DeletePageView.as_view(), name="delete"),


]