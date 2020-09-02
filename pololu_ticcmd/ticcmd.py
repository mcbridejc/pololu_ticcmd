import subprocess
from typing import List

def list_serials() -> List[str]:
    """Return a list of serial numbers detected
    """
    return []

def run_cmd(serial, args: List[str]):
    command = ['ticcmd']
    if serial is not None:
        command += ['-d', serial] 
        
    command += args

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    if result.returncode != 0:
        cmd_s = " ".join(command)
        raise RuntimeError(f"Error executing \"{cmd_s}\": {str(result.stdout.decode('utf-8'))}")

def set_options(
    serial: str=None,
    max_speed: int=None,
    starting_speed: int=None,
    max_accel: int=None,
    max_decel: int=None,
    step_mode: str=None,
    current: int=None):

    command = ["ticcmd"]
    if max_speed is not None:
        command += ['--max-speed', str(max_speed)]
    if step_mode is not None:
        command += ['--step-mode', step_mode]

    run_cmd(serial, command)

def home_forward(serial: str=None):
    run_cmd(serial, ['--home', 'fwd'])

def home_reverse(serial: str=None):
    run_cmd(serial, ['--home', 'rev'])

def position_relative(pos: int, serial: str=None):
    run_cmd(serial, ['--resume', '--position-relative', str(pos)])

def position(pos: int, serial: str=None):
    run_cmd(serial, ['-p', str(pos)])

def energize(serial: str=None):
    run_cmd(serial, ['--energize'])

def deenergize(serial: str=None):
    run_cmd(serial, ['--deenergize'])

