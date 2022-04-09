from django.urls import path
from .views import (
    homePageViews,
    HomePageViews,
    AboutPageView,
    Calculator,
)

urlpatterns = [
    path("", homePageViews, name="yuq"),
    path("home/", HomePageViews.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("cal/", Calculator.as_view(), name="calcu"),
]
