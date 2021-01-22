import subprocess
from time import sleep

# RUN THIS AS SUDO

# make sure to start postgres first so the rest of the containers can have data
subprocess.call(['sudo', 'docker', 'start' , 'postgres'])
#sleep to avoid the connection error with awx
sleep(60)
subprocess.call(['sudo', 'docker', 'start' , 'rabbitmq'])
sleep(10)
subprocess.call(['sudo', 'docker', 'start' , 'memcached'])
sleep(10)
subprocess.call(['sudo', 'docker', 'start' , 'awx_web'])
sleep(10)
subprocess.call(['sudo', 'docker', 'start' , 'awx_task'])
