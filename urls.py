"""
URL configuration for empproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.CreateEmployeeAPIView.as_view(), name='create_employee'),
    path('update/<int:employee_id>/', views.UpdateEmployeeAPIView.as_view(), name='update_employee'),
    path('list/', views.ListEmployeesAPIView.as_view(), name='list_employees'),
    path('delete/<int:employee_id>/', views.DeleteEmployeeAPIView.as_view(), name='delete_employee'),
    # Add more URL patterns as needed
]