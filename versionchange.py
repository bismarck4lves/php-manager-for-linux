import os
from phpackage import PhpVersion

class changeVersion:

    def __init__(self):
        
        php_in_use = PhpVersion().check_verison()
        not_in_use_versions = PhpVersion().list_no_used_versions()

        print('+------------------+')
        print('+ Versão  | Opções |')
        print('+------------------+')
        print('+   {}   | ativo  | <--'.format(php_in_use))

        for i, version in enumerate(not_in_use_versions, start=0):
            print('+------------------+')
            print("|   {}   |   {}    |".format(version, i))
        
        print('+------------------+')

        version_chousen = int(input("\nInforme a Opção de versão desejada: "))
        version_chousen = not_in_use_versions[version_chousen]

        swicht_log = PhpVersion().swicth_versions(version_chousen)
        
        print (swicht_log)