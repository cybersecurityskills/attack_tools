import paramiko

host = "192.168.100.2"
username = "root"
passwords = ["not_correct_passwd","not_correct_password","not_correct_password","not_correct_password","not_correct_password","not_correct_password","not_correct_password","not_correct_password"]

for password in passwords:
   print("Trying password: [%s]" % password)
   client = paramiko.client.SSHClient()
   client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   try:
      client.connect(host,username=username,password=password,timeout=5)
   except paramiko.ssh_exception.AuthenticationException as e:
      if str(e) == 'Authentication failed.':
         print("Auth failed, trying again")
