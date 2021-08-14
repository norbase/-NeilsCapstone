from django.urls import path
from .views import homepage, all_workouts


app_name = "contacts"
urlpatterns = [
    path("", homepage, name="home"),
    path("all/", all_workouts, "all_workouts")
]
