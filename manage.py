from versionchange import changeVersion

print("+--------+-------------------------------------------+")
print("+ Opção  +   Descição                                +")
print("+--------+-------------------------------------------+")
print("|   0    |   Mudar versão do php                     |")
print("+--------+-------------------------------------------+")
print("|   1    |   Instalar dependencias de uma versão     |")
print("+--------+-------------------------------------------+")

chousen = int(input("Escoloha uma opção: "))

if chousen == 0:
    changeVersion()