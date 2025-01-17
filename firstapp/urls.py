from django.urls import path
from . import views

urlpatterns = [
    path('', views.options_view, name='options'),
    path('', views.enter_data_view, name='enter_data'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('success/', views.success_view, name='success'),
]
