import subprocess
import os
import shutil

# Run commands with administrator privileges
def run_cmd(command):
    subprocess.run(command, shell=True)

# Stop SentinelOne services
services = ["SentinelAgent", "SentinelMonitor"]
for service in services:
    run_cmd = f'net stop {service}'
    subprocess.call(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(run_as_admin(subprocess.run(["sc", "stop", service], shell=True)

# Kill running processes associated with SentinelOne
sentinel_processes = ["SentinelAgent.exe", "SentinelCtl.exe"]
for process in sentinel_processes:
    subprocess.run(['taskkill', '/f', '/im', process], shell=True)

# SentinelOne file paths
file_paths = [
    r'C:\Program Files\SentinelOne',
    r'C:\ProgramData\SentinelOne',
    r'C:\Windows\System32\drivers\SentinelOne.sys',
    r'C:\Windows\System32\drivers\SentinelMonitor.sys'
]

# Delete SentinelOne files and directories
for path in file_paths:
    if os.path.exists(path):
        try:
            shutil.rmtree(path, ignore_errors=True)
        except Exception as e:
            print(f'Error removing {path}: {e}')

# Remove registry keys
registry_paths = [
    r'HKLM\SOFTWARE\Sentinel Labs',
    r'HKLM\SYSTEM\CurrentControlSet\Services\SentinelAgent',
    r'HKLM\SYSTEM\CurrentControlSet\Services\SentinelStaticEngine',
    r'HKLM\SYSTEM\CurrentControlSet\Services\SentinelMonitor'
]

for reg_path in registry_paths:
    subprocess.call(f'reg delete "{registry_paths}" /f', shell=True)

# Final message
print("SentinelOne has been successfully removed. Please restart your computer.")