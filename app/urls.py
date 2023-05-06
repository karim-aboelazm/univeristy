from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView 

app_name = "app"

urlpatterns = [
    path("",HomePageView.as_view(),name="home"),
    path("doctors/",DoctorsPageView.as_view(),name="doctors"),
    path("students/",StudentsPageView.as_view(),name="students"),
    path("search/",SearchView.as_view(),name="search"),
    path("halls/",HallsPageView.as_view(),name="halls"),
    path('login/', MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
]
