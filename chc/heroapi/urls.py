from django.urls import path
from heroapi import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('company/', views.CompanyList.as_view(), name = 'company'),
    path('employees/', views.EmployeesList.as_view(), name = 'employees'),
    path('company/<str:cnpj>', views.FilterCompany.as_view(), name = 'company'),
    path('employees/<str:name>/', views.FilterEmployees.as_view(), name = 'employees')
]
