from django.urls import path
from . import views


urlpatterns = [
    path("", views.show_all_message),
    path('save_json/', views.save_json, name='save_json'),
]
