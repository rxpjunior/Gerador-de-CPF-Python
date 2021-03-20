import random

# Sorteando os nove primeiros numeros aleatórios
numerosCpf = []
for x in range(9):
    numerosCpf.append(str(random.randint(0, 9)))
print(numerosCpf)
cpf = "".join(numerosCpf)

# Calculo do primeiro Digito
cpf = cpf[::-1]
listaMultiplos = []
for x, y in enumerate(cpf, 2):
    listaMultiplos.append(x * int(y))
aux = 11 - (sum(listaMultiplos) % 11)
if aux > 9:
    primeiroDigito = "0"
else:
    primeiroDigito = str(aux)
cpf = cpf[::-1]
cpf += primeiroDigito
cpf = cpf[::-1]

# Calculo do segundo Digito
listaMultiplos = []
for x, y in enumerate(cpf, 2):
    listaMultiplos.append(x * int(y))
segundoDigito = 11 - (sum(listaMultiplos) % 11)
cpf = cpf[::-1]
cpf += str(segundoDigito)
print(cpf)

