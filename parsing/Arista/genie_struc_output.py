from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_scrapli.functions import print_structured_result
from nornir_utils.plugins.functions import print_result
import ipdb



nr = InitNornir(config_file="config.yaml")

def parse(task):
    int_result = task.run(task=send_command, command="sh int desc ")
    task.host["facts"] = int_result.scrapli_response.genie_parse_output()
    
    



result = nr.run(task=parse)
print_structured_result(result, parser="genie")
#ipdb.set_trace()
