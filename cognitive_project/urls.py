"""
URL configuration for cognitive_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cognitive import views
from cognitive.views import UpdateAttemptView, GetAttemptView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.register_user, name='register_user'),
    path('api/save_test_result/', views.save_test_result, name='save_test_result'),
    path('api/login/', views.login_user, name='login_user'),
    path('update-attempt/', UpdateAttemptView.as_view(), name='update-attempt'),
    path('get-attempt/', GetAttemptView.as_view(), name='get-attempt'),
]
