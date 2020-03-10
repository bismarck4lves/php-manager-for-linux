import os

class PhpVersion:

    def __init__(self):

        self.php_list = os.listdir('/etc/php')
        
        self.shell_request = os.popen("php -v").read()

    def check_verison(self):

        for version in self.php_list:

            model = "PHP {}".format(version)

            if self.shell_request.count(model) != 0:

                return model.replace("PHP ", "")

        return False

    def list_no_used_versions(self):

        new_list = []

        for item in self.php_list:
        
            if self.check_verison() != item:
        
                new_list.append(item)

        return new_list

    def swicth_versions(self, version_chousen):

        actions_commands = [
            "sudo update-alternatives --set php /usr/bin/php{}".format(version_chousen),
            "sudo a2dismod php{}".format(self.check_verison()),
            "sudo a2enmod php{}".format(version_chousen),
            "sudo systemctl restart apache2",
            "php -v"
        ]

        log = ''

        for command in actions_commands:

            log += os.popen(command).read() + "\n"

        return log