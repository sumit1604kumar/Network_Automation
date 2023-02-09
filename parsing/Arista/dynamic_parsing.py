from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb
from rich import rprint as rprint


nr = InitNornir(config_file="config.yaml")

def parse(task):
    version = task.run(task=send_command, command="sh ip bgp summary")
    task.host["facts"] = version.scrapli_response.textfsm_parse_output()
    neighbours = task.host["facts"]["vrf"]["default"]["neighbour"]
    for key in neighbours:
        updown = neighbour[key]["address_family"][""]["up_down"]
        rprint(f"{task.host} neighbour{key} updown value is {updown}")
    #uptime = task.host["facts"]["version"]["uptime"]
    #print(uptime)



result = nr.run(task=parse)
#print_result(result)
#ipdb.set_trace()
