from django.urls import path
from .views import DashboardView

app_name = "influencers"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
]
