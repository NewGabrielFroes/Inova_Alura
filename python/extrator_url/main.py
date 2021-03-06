url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
# url = "                    "
print(url)

# Sanitizacao da url
url = url.strip()

# Validacao da url
if url == "":
    raise ValueError("A URL está vazia")

# Separa a base e os parâmetros
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
tamanho_parametro = len(parametro_busca)
indice_valor = indice_parametro + tamanho_parametro + 1
indice_e_comercial = url_parametros.find("&", indice_valor)
valor = url_parametros[indice_valor:indice_e_comercial]
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
