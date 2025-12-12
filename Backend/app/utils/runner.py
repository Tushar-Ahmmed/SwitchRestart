import ansible_runner

def run_playbook(playbook: str, extravars: dict = None):
    """
    Runs an Ansible playbook using ansible-runner.

    Parameters:
        playbook (str): The playbook filename (inside the ansible/ directory)
        extravars (dict): Extra variables for Ansible

    Returns:
        dict: result including status, rc, stdout, stderr
    """
    print("Successfully called")
    result = ansible_runner.run(
        private_data_dir="ansible",
        playbook="restart-switch.yml" or playbook,
        extravars=extravars.location or {}
    )

    # Format results for FastAPI
    output = {
        "status": result.status,
        "rc": result.rc,
        "stdout": result.stdout.read() if result.stdout else "",
        "stderr": result.stderr.read() if result.stderr else "",
    }

    return output
