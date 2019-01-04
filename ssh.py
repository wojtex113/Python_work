import paramiko

p=22
u='admin'
pas='c37s258'
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
'172.4.1.211',
'172.4.1.212',
'172.4.1.213',
'172.4.1.215',
'172.4.1.216',
'172.4.1.229',
'172.4.1.230',
'172.4.1.231',
'172.4.1.232',
'172.4.1.233',
'172.4.1.234',
'172.4.1.236',
'172.4.1.237',
'172.4.1.238',
'172.4.1.239',
'172.4.1.240',
'172.4.1.241'
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
