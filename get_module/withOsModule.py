from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import os


nr = InitNornir(config_file="config.yaml")

nr.inventory.defaults.username = os.environ["USERNAME"]
nr.inventory.defaults.password = os.environ["PASSWORD"]


def get_password(task):
    task.run(task=send_command, command="show ip int brief" )

result= nr.run(task=get_password)
print_result(result)


please note : uername and password will be mention in the bash file of the linux.
  
  nano ~/.bashrc
  
  export USERNAME=sumit
  export PASSWORD=cisco
