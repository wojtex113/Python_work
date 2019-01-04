import paramiko

p=22
u='ssh_unifi_ap_login'
pas='ssh_unifi_ap_password'
wykonano=0

komendy_sprawdzenie=[
"cat /var/etc/persistent/cfg/blocked_sta"
]

komendy_czyszczenie=[
"cat /var/etc/persistent/cfg/blocked_sta",
"mv /var/etc/persistent/cfg/blocked_sta /var/etc/persistent/cfg/blocked_sta_old",
"touch /var/etc/persistent/cfg/blocked_sta",
"ls -l /var/etc/persistent/cfg/"
]

hosty=[
'ip_unifi_ap',
'ip_unifi_ap'
]

for host in hosty:
	print("#############################")
	print(host)
	print("#############################")
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host,port=p,username=u,password=pas)
	wykonano += 1

	for kome in komendy_sprawdzenie:
		stdin,stdout,stderr=ssh.exec_command(kome)
		output=stdout.readlines()
		if output==[]:
			print("Plik pusty")
		else:
			for kom in komendy_czyszczenie:
				stdin,stdout,stderr=ssh.exec_command(kom)
				output=stdout.readlines()
				print("".join(output))

	ssh.close()

print("\nWykonano na %d z %d hostow"%(wykonano,len(hosty)))
