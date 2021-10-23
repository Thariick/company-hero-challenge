from rest_framework import serializers
from .models import Company, Employees

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model= Company
        fields='__all__'
    
class EmployeesSerializer(serializers.ModelSerializer):  
    class Meta:
        model= Employees
        fields='__all__'