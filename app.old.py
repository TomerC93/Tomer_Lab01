import boto3
import os
import time

def pull_online_machines():
        ec2 = boto3.resource('ec2')

        for instance in ec2.instances.all():
                 kube_machine = False
                        for tag in instance.tags:
                          if tag['Value'] == "1" and tag['Key'] == "k8s.io/role/master" and instance.state["Code"] == 16:
                             kube_machine = True
                          if kube_machine == True:
                           for tag in instance.tags:
                            if tag['Key'] == "Name":
                             print("{0} {1}".format(tag['Value'], instance.id))
                        
                        
interval = os.environ.get('INTERVAL')
if interval == None:
    pull_online_machines()
else:
    while True:
        pull_online_machines()
        print("Sleep for {0} seconds".format(interval))
        time.sleep(int(interval))
