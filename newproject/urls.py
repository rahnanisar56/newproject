from django.urls import path
from website import views
urlpatterns = [
  path('', views.homepagee),
  path('about/',views.aboutt),
  path('homepage/',views.homepagee)
]