import subprocess
from time import sleep

# RUN THIS AS SUDO


subprocess.call(['sudo', 'docker', 'stop', '--time=30' , 'postgres'])
sleep(5)
subprocess.call(['sudo', 'docker', 'stop', '--time=30' , 'rabbitmq'])
sleep(5)
subprocess.call(['sudo', 'docker', 'stop', '--time=30' , 'memcached'])
sleep(5)
subprocess.call(['sudo', 'docker', 'stop', '--time=30' , 'awx_web'])
sleep(5)
subprocess.call(['sudo', 'docker', 'stop', '--time=30' , 'awx_task'])
