from utils.runner import run_playbook
def switch_restart_service(location:str):
    run_playbook("Demo",{"location":location})