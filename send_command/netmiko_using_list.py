from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

my = ["show int desc", "show ip int brief"]

def show_test(task):
    for x in my:
        task.run(task=netmiko_send_command, command_string=x)

result = nr.run(task=show_test)
print_result(result)
