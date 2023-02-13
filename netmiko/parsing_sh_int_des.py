from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr=InitNornir(config_file="config.yaml")

def clock(task):
    clock_result = task.run(task=netmiko_send_command, command_string="show int desc", use_textfsm=True)

    output = clock_result.result
    print(output)

result = nr.run(task=clock)
#print_result(result)
