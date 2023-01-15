from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import getpass

nr = InitNornir(config_file="config.yaml")
password = getpass.getpass()
nr.inventory.defaults.password = password

def get_password(task):
    task.run(task=send_command, command="show ip int brief" )

result= nr.run(task=get_password)
print_result(result)
