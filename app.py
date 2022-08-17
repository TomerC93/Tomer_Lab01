import boto3
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
