import spur
host="172.31.18.170"
shell = spur.SshShell(hostname=host, username="ec2-user", private_key_file="/home/ec2-user/keys/NagiosKey.pem" , missing_host_key=spur.ssh.MissingHostKey.accept)
with shell:
    result = shell.run(["free","-m"])
status_file=open("status_file.txt","w")
status_file.write("------------------------------------------------"+host+"-----------------------------------------------"+"\n\n")
status_file.write(result.output)
status_file.write("---------------------------------------------------end----------------------------------------------------"+"\n\n")
status_file.close()
