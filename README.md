# DEBUG SMTP

## Overview

This script will help you debug an SMTP Session.

## Usage

	-s, --server [SMTP SERVER ADDRESS / IP]
	The SMTP Server you want to test

	-f, --from [FROM ADDRESS]
	The e-mail address you want to use to send the testmail

	-t, --to [TO ADDRESS]
    The reciever of the testmail.

	-h, --help
    Shows a quick help-message

## Example

Sending an testmail to user2@example.org via smtp.gmail.com

	$ ./debugSMTP.py -s smtp.gmail.com -f user1@example.org -t user2@example.org

Output:

	reply: '250-mx.google.com at your service, [87.79.252.38]\r\n'
	reply: '250-SIZE 35882577\r\n'
	reply: '250-8BITMIME\r\n'
	reply: '250-STARTTLS\r\n'
	reply: '250-ENHANCEDSTATUSCODES\r\n'
	reply: '250-PIPELINING\r\n'
	reply: '250-CHUNKING\r\n'
	reply: '250 SMTPUTF8\r\n'
	reply: retcode (250); Msg: mx.google.com at your service, [87.79.252.38]
	SIZE 35882577
	8BITMIME
	STARTTLS
	ENHANCEDSTATUSCODES
	PIPELINING
	CHUNKING
	SMTPUTF8
	send: 'mail FROM:<user1@example.org> size=227\r\n'
	reply: '530 5.7.0 Must issue a STARTTLS command first. v3sm11736716wiz.14 - gsmtp\r\n'
	reply: retcode (530); Msg: 5.7.0 Must issue a STARTTLS command first. v3sm11736716wiz.14 - gsmtp
	send: 'rset\r\n'
	reply: '250 2.1.5 Flushed v3sm11736716wiz.14 - gsmtp\r\n'
	reply: retcode (250); Msg: 2.1.5 Flushed v3sm11736716wiz.14 - gsmtp
	Error:
	send: 'quit\r\n'
	reply: '221 2.0.0 closing connection v3sm11736716wiz.14 - gsmtp\r\n'
	reply: retcode (221); Msg: 2.0.0 closing connection v3sm11736716wiz.14 - gsmtp

In this example the try fails because gmail only accepts tls connections. 

## Contact

You can contact me via mail: [mail@sysadmin-log.de](mail@sysadmin-log.de).
