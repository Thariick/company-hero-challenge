from warnings import catch_warnings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Company, Employees
from .serializer import CompanySerializer, EmployeesSerializer
from .forms import RegistrationForm

def index(request):
    form = RegistrationForm()
    context = {
        "companyform": form
    }
    return render(request, "heroapi/index", context)


class CompanyList(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeesList(APIView):
    def get(self, request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FilterEmployees(APIView):
    def get(self, request, name):
        get_employees = Employees.objects.filter(name = name)
        if get_employees:
            employees = {}
            companies = []
            for employee in get_employees:
                employees['name'] = employee.name
                employees['cpf ou rg'] = employee.cpf_ou_rg
                employees['cargo'] = employee.cargo
                company = Company.objects.get(pk=employee.company_id)
                companies.append(company.razao_social)
            employees['companies'] = companies
            return JsonResponse(employees, status=200)
        return JsonResponse({'error': 'Funcionario não encontrado!'}, status=404)

class FilterCompany(APIView):

    def get(self, request, cnpj):
        get_company = Company.objects.filter(cnpj=cnpj)
        if get_company:
            companied = {}
            employee = []
            employees = []
            for company in get_company:
                companied['razao_social'] = company.razao_social
                companied['nome_fantasia'] = company.nome_fantasia
                companied['telefone_comercial'] = company.telefone_comercial
                companied['inscricao_municipal_estadual'] = company.inscricao_municipal_estadual
                companied['cnpj'] = company.cnpj
                companied['endereco'] = company.endereco
                companied['email'] = company.email
                employeer = Employees.objects.filter(company=company.id)
                for employ in employeer:
                    employees.append(employ.name)
            companied['employeers'] = employees
            return JsonResponse(companied, status=200)
        return JsonResponse({'error': 'Empresa não encontrado!'}, status=404)
