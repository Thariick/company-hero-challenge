from django.urls import path, include
from heroapi import views
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'forms', views.Forms, basename = "forms")

urlpatterns = [
    path('', include(route.urls)),
    path('companies/', views.CompaniesList.as_view(), name = 'company'),
    path('employees/', views.EmployeesList.as_view(), name = 'employeer'),
    path('company/<str:cnpj>', views.CompanyFilter.as_view(), name = 'company'),
    path('employee/<str:name>/', views.EmployeeFilter.as_view(), name = 'employees')
    ]