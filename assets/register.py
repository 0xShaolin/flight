##registration application!!!

try: #handle imports
	import getpass, bcrypt
except ImportError:
	print "Missing bcrypt... failing..."
	import sys; sys.exit(1)

credlist = open('~/flight/assets/creds.txt', 'r+')

def getCreds():
	while True: #while loop to allow for error
		user = raw_input('Username: ')
		if user in credlist.read():
			print "Username already taken."
		else:
			verify = raw_input('Are you sure you want username ' + user + ': ')
			if verify == 'y' or verify == 'yes':
				break
			else:
				continue
	while True: #now checking if pass meets requirements
		password = getpass.getpass('Password: ')
		if len(password) < 5 or len(password) > 25:
			print "Password must be between 5 and 25 charactees."
		else:
			break
	password = bcrypt.hashpw(password, bcrypt.gensalt())
	cred = user + ':' + password
	return cred

def writeCreds(creds):
	credlist.write(creds)

credlist.close()

print "Registration complete! Please remember your login!"
