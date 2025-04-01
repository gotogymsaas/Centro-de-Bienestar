from django.urls import path
from .views import NPSChartView, GroupChartView


urlpatterns = [
    path("nps", NPSChartView.as_view(), name="nps_chart"),
    path("group-chart/", GroupChartView.as_view(), name="group_chart"),

]
