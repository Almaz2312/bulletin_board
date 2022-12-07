import django.contrib.auth.views
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('activate/<uid64>/<token>', views.VerificationView.as_view(), name='activate'),
    path('private/', views.private, name='private'),
]

