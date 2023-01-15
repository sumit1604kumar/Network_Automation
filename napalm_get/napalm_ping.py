from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def napalm_send(task):
    task.run(task=napalm_ping, dest="8.8.8.8")

result = nr.run(task=napalm_send)
print_result(result)
