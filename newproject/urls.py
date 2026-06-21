from django.urls import path
from website import views
urlpatterns = [
  path('', views.website),
  path('/',views.homepage),
  path('/about',views.about)
]