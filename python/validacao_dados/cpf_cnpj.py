from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta")

class DocCpf:
    def __init__(self, documento):
        self.cpf = documento
        if not self.valida():
            raise ValueError("CPF inválido")

    def valida(self):
        validador = CPF()
        return validador.validate(self.cpf)

    def __str__(self):
        return self.format()

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        self.cnpj = documento
        if not self.valida():
            raise ValueError("CNPJ inválido")

    def valida(self):
        validador = CNPJ()
        return validador.validate(self.cnpj)

    def __str__(self):
        return self.format()

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
