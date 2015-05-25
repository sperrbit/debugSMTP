#!/usr/bin/python

# ******************************************
#  SMTP Debugger
#  Version 1.1
#  Christoph Franke
#  19.04.2015
# *****************************************

import smtplib
import argparse

parser = argparse.ArgumentParser(description='debugSMTP')
parser.add_argument('-s', '--server', help='SMTP Server', required=True)
parser.add_argument('-f','--from' ,help='From Address', required=True)
parser.add_argument('-t','--to', help='To Address', required=True)

args = vars(parser.parse_args())
vserver = str(args['server'])
vfrom = str(args['from'])
vto = str(args['to'])
vmessage = 'From: '+vfrom+'\nTo:'+vto+'\nSubject: * Testmail *\n\nMit dieser E-Mail wurde die SMTP Verbindung zur Ihrem Mail-Server getestet.\nSie brauchen nicht auf diese E-Mail zu antworten. Sie koennen diese E-Mail loeschen'

server = smtplib.SMTP(vserver)
server.set_debuglevel(1)
try:
    server.sendmail(vfrom,vto,vmessage)
except smtplib.SMTPException, e:
    print "Error:", e.message
server.quit()
