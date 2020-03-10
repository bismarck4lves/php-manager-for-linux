import os
from phpackage import PhpVersion

php_version = PhpVersion().check_verison()

dependence_list = open('./base_dependences/php{}.txt'.format(php_version), 'r')

print("As seguintes depencias serão instalas em seu php{}:".format(php_version))

for dependence in dependence_list:
    print(dependence)

confirm = input("\ndeseja continuar?[s/n]?: ")


if confirm == 's' or confirm == 'S':
    for dependence in dependence_list:
        print(os.popen("sudo apt-get install php{}-{}".format(php_version, dependence)).read())

elif confirm == 'n' or confirm == 'N':

    print ("Oparação cancelda pelo usuário!")
else:

    print ("Operação cancelda! Argumentos não satisfatórios!")
