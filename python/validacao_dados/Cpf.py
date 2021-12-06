from validate_docbr import CPF


class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!")


    def cpf_e_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            return ValueError("Quantidade de digitos inválida")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()