from django.urls import path
from .views import DashboardView, InfluencerRegisterView

app_name = "influencers"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("registro/", InfluencerRegisterView.as_view(), name="register"),
]
