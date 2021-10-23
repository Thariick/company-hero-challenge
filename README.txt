***GITHUB: https://github.com/Thariick/company-hero-challenge***
***HEROKU: companyherochallenge***
OBS: NÃO FOI POSSÍVEL SUBIR O APP NO HEROKU, POR ALGUM MOTIVO ESTÁ DANDO DIVERGÊNCIA NA VERSÃO DO BUILDPACKS, OU ALGO DO TIPO, NÃO SEI DIZER O QUE É, TENTEI 12 VEZES E NÃO FOI POSSÍVEL ARRUMAR, DESCULPA!

-> Breve descrição de como foi feito a API e como utilizar e suas respostas:
- Criar formulário para empresa: 
	razao_social, nome_fantasia, telefone, cnpj, endereco e email.
- Criar os models para empresa e funcionários (precisa de foreign key para relacionar com company);
- Criar o serializer;
- Criar o Views;
- Criar URLs;
- Realizar testes; (Colocar app instalado nos settings)

- Descrição de como utilizar API com Postman:
-> Response do GET empresas:
{
        "id": 1,
        "razao_social": "Company Hero",
        "nome_fantasia": "Company Hero",
        "telefone": "99999999999",
        "cnpj": "12345678901234",
        "endereco": "Avenida Rua",
        "email": "people@companyhero.com"
}

-> Response do GET para CNPJ:
{
    "razao_social": "Company Hero",
    "nome_fantasia": "Company Hero",
    "telefone": "99999999999",
    "cnpj": "12345678901234",
    "endereco": "Avenida Rua",
    "email": "people@companyhero.com",
    "employees": [
        "Tharick Almeida"
    ]
}

-> Response do GET para empresas que não são encontradas:
{
    "Empresa não encontrada!"
}

-> POST:
{
    "razao_social": "Razão social"(String),
    "nome_fantasia": "Nome fantasia"(String),
    "telefone": "Telefone da empresa"(String),
    "cnpj": "CNPJ"(String),
    "endereco": "Endereço"(String),
    "email": "email"(String)
}

-> Response do GET funcionários:
{
        "id": 1,
        "name": "Tharick ALmeida",
        "cargo": "dev python jr",
        "cpf ou rg": "00895249936",
        "company": 1
}

-> Response do GET para name:
{
    "name": "Tharick Almeida",
    "cpf ou rg": "00895249936",
    "cargo": "dev python jr",
    "companies": [
        "Company Hero"
    ]
}
-> Response do GET para funcionários não encontrados:
{
    "Funcionário não encontrado!"
}

-> POST:
{
    "name": "nome do funcionario"(String),
    "cargo": "cargo do funcionario"(String),
    "cpf ou rg": "cpf do funcionario"(String),
    "company": "id da company"(String)
}



