from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

command_list = ["show run", "show version", "show ip int brief"]

nr = InitNornir(config_file="config.yaml")
def random_config(task):
    for cmd in command_list:
        task.run(task=send_command, command=cmd)

results = nr.run(task=random_config)
print_result(results)
