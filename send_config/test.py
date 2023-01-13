from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def send_config_test(task):
    task.run(task=send_config, config="router bgp 100")

result=nr.run(send_config_test)
print_result(result)
