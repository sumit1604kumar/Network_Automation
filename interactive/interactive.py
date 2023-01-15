from nornir import InitNornir
from nornir_scrapli.tasks import send_command #send_interactive
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def interactive_send(task):
    #cmd =[("copy run flash:patel", "destination filename"),(f"{task.host}#")]
    task.run(task=send_command, command="config replace flash:sumit ignore-errors")

result = nr.run(task=interactive_send)
print_result(result)

