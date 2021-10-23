from django.db import models

class Company(models.Model):
    razao_social  = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.razao_social


class Employees(models.Model):
    name = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    cpf_ou_rg = models.CharField(max_length=50)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='company')

    def __str__(self):
        return self.name
