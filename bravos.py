import datetime
import csv
import time
from datetime import date
from time import strftime
import smtplib

def gamepull(data,dictionary):
	with open(data,mode='r') as table:
		reader = csv.reader(table)
		for row in reader:
			dictionary.update({row[0]:row[1:]})

def phonepull(data,dictionary):
	with open(data,mode='r') as table:
		reader = csv.reader(table)
		for row in reader:
			dictionary.update({row[0]:row[1]})

	
def reminder(dictionary,phonelist,phonedata):
	gamelist = dictionary[today.strftime("%Y-%m-%d")]
	gametime = gamelist[1]
	gameloc = gamelist[2]
	tvstat = gamelist[3]
	opp = gamelist [4]
	x = datetime.datetime.now()
	remindertime = datetime.datetime.strptime('{} {}' .format(today,gamelist[0]),"%Y-%m-%d %H:%M")
	print ('Reminder to go out at {}' .format(remindertime))
	secondstilreminder = remindertime-x
	
	while x < remindertime:
		print("need to wait {} sec until reminder time!" .format(secondstilreminder.seconds))
		time.sleep(10)
		x = datetime.datetime.now()
		secondstilreminder = remindertime-x
	
	#sends email/txt
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("emailaddy", "PW_redacted")
	#one email/txt per phone in phone list
	phonepull(phonedata,phonelist)
	for name, email in phonelist.items():
		msg = '\n\n Hello {}! \nBraves are on at {}, broadcasting on {} \n{} versus {}' .format(name,gametime,tvstat,gameloc,opp)
		server.sendmail('emailaddy', email,msg)
	server.quit()

def gamecheck(today,dictionary,phonelist,phonedata):
	if today.strftime("%Y-%m-%d") in dictionary:
		print ('Aww yiss the bravos are playing today!')
		reminder(dictionary,phonelist,phonedata)
	else:
		print("No Braves games today!  Womp womp")
		


games_dict={}
phonelist = {}
today = date.today()

gamepull('braves.csv',games_dict)
gamecheck(today,games_dict,phonelist,'phone.csv')

	


