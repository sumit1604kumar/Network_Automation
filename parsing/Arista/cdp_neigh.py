from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result
import ipdb
#from rich import rprint as rprint


nr = InitNornir(config_file="config.yaml")

def parse(task):
    version = task.run(task=send_command, command="sh cdp neighbour")
    task.host["facts"] = version.scrapli_response.textfsm_parse_output()
    cdp_index = task.host["facts"]["cdp"]["index"]
    for num in cdp_index:
        local_int  = cdp_index[num]["local_interface"]
        remote_port  = cdp_index[num]["port_id"]
        remote_device  = cdp_index[num]["device_id"]

        config_commands =[f"interface{local_int}", f"description connected to {remote_device} via its {remote_device} "] 
        task.run(task=send_config, config=config_commands)
#
    #uptime = task.host["facts"]["version"]["uptime"]
    #print(uptime)



result = nr.run(task=parse)
print_result(result)
#ipdb.set_trace()
