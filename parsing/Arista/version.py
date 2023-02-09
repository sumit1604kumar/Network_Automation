from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb


nr = InitNornir(config_file="config.yaml")

def parse(task):
    version = task.run(task=send_command, command="sh int desc ")
    task.host["facts"] = version.scrapli_response.textfsm_parse_output()
    #print(task.host["facts"])
    #uptime = task.host["facts"]["version"]["uptime"]
    #print(uptime)



result = nr.run(task=parse)
#print_result(result)
ipdb.set_trace()


*****************************************************************OUTPUT********************************888
ipdb> nr.inventory.hosts["R1"]["facts"]
[{'port': 'Et1', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et2', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et3', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et4', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et5', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et6', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et7', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et8', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Ma1', 'status': 'up', 'protocol': 'up', 'descrip': ''}]
ipdb> 
[{'port': 'Et1', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et2', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et3', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et4', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et5', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et6', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et7', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Et8', 'status': 'up', 'protocol': 'up', 'descrip': ''}, {'port': 'Ma1', 'status': 'up', 'protocol': 'up', 'descrip': ''}]
ipdb> pp nr.inventory.hosts["R1"]["facts"]
[{'descrip': '', 'port': 'Et1', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et2', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et3', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et4', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et5', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et6', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et7', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et8', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Ma1', 'protocol': 'up', 'status': 'up'}]
ipdb> 
[{'descrip': '', 'port': 'Et1', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et2', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et3', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et4', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et5', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et6', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et7', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et8', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Ma1', 'protocol': 'up', 'status': 'up'}]
ipdb> 
[{'descrip': '', 'port': 'Et1', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et2', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et3', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et4', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et5', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et6', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et7', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Et8', 'protocol': 'up', 'status': 'up'},
 {'descrip': '', 'port': 'Ma1', 'protocol': 'up', 'status': 'up'}]
ipdb> pp nr.inventory.hosts["R1"]["facts"]["Et1"]
*** TypeError: list indices must be integers or slices, not str
ipdb> 
*** TypeError: list indices must be integers or slices, not str
ipdb> 
*** TypeError: list indices must be integers or slices, not str
ipdb>  nr.inventory.hosts["R1"]["facts"]["Et1"]
*** TypeError: list indices must be integers or slices, not str
ipdb> pp nr.inventory.hosts["R1"]["facts"]["descrip"]]
*** SyntaxError: unmatched ']'
ipdb> pp nr.inventory.hosts["R1"]["facts"]["port"]
*** TypeError: list indices must be integers or slices, not str
ipdb> 
*** TypeError: list indices must be integers or slices, not str
ipdb> 
*** TypeError: list indices must be integers or slices, not str
ipdb> 
*** TypeError: list indices must be integers or slices, not str
ipdb> pp nr.inventory.hosts["R1"]["facts"][0]]
*** SyntaxError: unmatched ']'
ipdb> pp nr.inventory.hosts["R1"]["facts"][0]
{'descrip': '', 'port': 'Et1', 'protocol': 'up', 'status': 'up'}
ipdb> 
{'descrip': '', 'port': 'Et1', 'protocol': 'up', 'status': 'up'}
ipdb> 
{'descrip': '', 'port': 'Et1', 'protocol': 'up', 'status': 'up'}
ipdb> 
{'descrip': '', 'port': 'Et1', 'protocol': 'up', 'status': 'up'}
ipdb> pp nr.inventory.hosts["R1"]["facts"][0]["port"]
'Et1'
ipdb> 
'Et1'
ipdb> 
