def inverte_texto(string):
  return string[::-1]

entrada = input("Digite um texto: ")
resultado = inverte_texto(entrada)
print("texto invertido é:", resultado)