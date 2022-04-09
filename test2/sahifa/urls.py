from django.urls import path
from .views import (
    HomePageViews,
    CalculatorViews,
)

urlpatterns = [
    path("", HomePageViews.as_view(), name="home"),
    path("calculator/", CalculatorViews.as_view(), name="calculator"),
]
