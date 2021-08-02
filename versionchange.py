from phpackage import PhpVersion
from utils import Tables

class changeVersion:

    def __init__(self):
        
        php_in_use = PhpVersion().check_verison()
        
        not_in_use_versions = PhpVersion().list_no_used_versions()

        valid_data = [['Versão', 'Opções']]
        
        valid_data.append([php_in_use, 'ativo <='])

        for i, version in enumerate(not_in_use_versions, start=0):
            
            valid_data.append([version, str(i)])
        
        Tables().load(valid_data)

        version_chousen = int(input("\nInforme a Opção de versão desejada: "))

        version_chousen = not_in_use_versions[version_chousen]

        swicht_log = PhpVersion().swicth_versions(version_chousen)
        
        print (swicht_log)