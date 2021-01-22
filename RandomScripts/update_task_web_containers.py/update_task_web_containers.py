"""
******************************************************************************
******************************************************************************
* This will erase all temporary files in the Docker image.                   *
* Anything that has been added by us will be erased. This includes installed * 
* programs and configurations. The only data that is retained is the data in * 
* the PostgreSQL container as it is a permanent volume(all playbooks and     *
* credentials reside in the PostgreSQL container)                            *
******************************************************************************
******************************************************************************
"""
import subprocess
from time import sleep

affirmation = raw_input("Have You Read The Warning in The File???? yes/no: ")
if (affirmation.upper() == 'YES'):
    print("starting update......(CTRL C) TO CANCEL")
    sleep(10)
    subprocess.call(['sudo', 'docker', 'stop' , 'awx_task'])
    sleep(10)
    subprocess.call(['sudo', 'docker', 'rm' , 'awx_task'])
    sleep(10)
    subprocess.call(['sudo', 'docker', 'rmi' , 'ansible/awx_task:latest'])
    sleep(10)
    subprocess.call(['sudo', 'docker', 'stop' , 'awx_web'])
    sleep(10)
    subprocess.call(['sudo', 'docker', 'rm' , 'awx_web'])
    sleep(10)
    subprocess.call(['sudo', 'docker', 'rmi' , 'ansible/awx_web:latest'])
    sleep(10)
    subprocess.call(['sudo', 'ansible-playbook', '-i' , 'inventory', 'install.yml'])
else:
    exit()

