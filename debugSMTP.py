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
vmessage = 'From: '+vfrom+'\nTo:'+vto+'\nSubject: * Testmail *\n\nMit dieser E-Mail wurde die SMTP Verbindung zur Ihrem Mail-Server getestet.\nSie brauchen nicht auf diese E-Mail zu antworten. Sie koennen diese E-Mail loeschen.\n\nMit freundlichen Gruessen,\n\nWolters Kluwer Deutschland ICT\n________________________________________\n\nWolters Kluwer Deutschland GmbH\n\nRobert-Bosch-Str. 6\n50354 Huerth\nTel +49 (221) 94373-7888\nE-Mail tec-support@wolterskluwer.de\n\nWolters Kluwer Deutschland GmbH | Luxemburger Strasse 449 | D-50939 Koeln | HRB 58843 Amtsgericht Koeln | Geschaeftsfuehrer: Dr. Ulrich Hermann (Vorsitz), Michael Gloss, Christian Lindemann, Frank Schellmann, Ralph Vonderstein | USt.-ID.Nr. 188836808\n\nConfidentiality Notice: This email and its attachments (if any) contain confidential information of the sender. The information is intended only for the use by the direct addressees of the original sender of this email. If you are not an intended recipient of the original sender (or responsible for delivering the message to such person), you are hereby notified that any review, disclosure, copying, distribution or the taking of any action in reliance of the contents of and attachmentsto this email is strictly prohibited. If you have received this email in error, please immediately notify the sender at the address shown herein and permanently delete any copies of this email (digital or paper) in your possession.'

server = smtplib.SMTP(vserver)
server.set_debuglevel(1)
try: 
    server.sendmail(vfrom,vto,vmessage)
except smtplib.SMTPException, e: 
    print "Error:", e.message
server.quit()
