from cpf_cnpj import Documento

exemplo_cpf = "15316264754"
exemplo_cnpj = "35379838000112"

documento = Documento.cria_documento(exemplo_cpf)
print(documento.valida())