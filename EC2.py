import time
from boto.ec2 import connect_to_region
ec2_conn=connect_to_region('us-west-2',aws_access_key_id='XXXXXXXXXXXXXXXX',aws_secret_access_key='XXXXXXXXXXXXXXXX')

demo_sg=ec2_conn.create_security_group("demo_sg","Demo security group")
demo_sg.authorize("tcp",22,22,"0.0.0.0/0")

demo_key=ec2_conn.create_key_pair("demo_key")
demo_key.save('.')

resrv=ec2_conn.run_instances("ami-775e4f16",key_name="demo_key",instance_type="t2.micro",security_groups=["demo_sg"])

demo=resrv.instances[0]
while demo.update() != "running":
	time.sleep(1)
print(demo.ip_address)