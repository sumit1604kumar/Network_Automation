from nornir import InitNornir
from nornir_scrapli.tasks import send_commands_from_file
from nornir_utils.plugins.functions import print_result

#command_list = ["show run", "show version", "show ip int brief"]

nr = InitNornir(config_file="config.yaml")
def random_config(task):
    task.run(task=send_commands_from_file, file="fileone.txt")

results = nr.run(task=random_config)
print_result(results)
