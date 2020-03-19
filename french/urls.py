from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('franchise/',views.franchise,name="franchise"),
    path('franchise/<int:fr_id>',views.display,name="display")
]
