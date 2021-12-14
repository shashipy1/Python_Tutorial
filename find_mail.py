import re

str = '''
Radharaman institute of technology and science bhopal
email : admission@radharamanbhopal.com

from:	PhonePe <noreply@phonepe.com>
to:	shashikant.skk.2016@gmail.com
date:	28 Sept 2021, 20:44
subject:	Unsure of investing in a high-flying market?
mailed-by:	delivery.mailer.phonepe.com
Signed by:	phonepe.com

from:	GeeksforGeeks <no-reply@geeksforgeeks.org>
to:	shashikant.skk.2016@gmail.com
date:	18 Sept 2021, 18:05
subject:	Fresh knowledge booster has arrived!
mailed-by:	us-west-2.amazonses.com
Signed by:	geeksforgeeks.org

from:	DSA INSTITUTE <imdigitalsandip@gmail.com> via getresponse-mail.com 
reply-to:	imdigitalsandip@gmail.com
to:	shashikant.skk.2016@gmail.com
date:	22 Sept 2021, 15:18
subject:	🤩Good News👉 Finally The Wait is Over!! We are Starting New Online Batch
mailed-by:	bounce.getresponse-mail.com
Signed by:	getresponse-mail.com

from:	PDF By Paola Flocchini <updates@academia-mail.com>
to:	shashikant.skk.2016@gmail.com
date:	4 Sept 2021, 05:27
subject:	📄 "Algorithms for Sensor Systems" by Paola Flocchini
mailed-by:	bounce.academia-mail.com
Signed by:	academia-mail.com

from:	Groww <noreply@groww.in>
to:	shashikant.skk.2016@gmail.com
date:	24 Sept 2021, 08:49
subject:	Inflation, stock market, and you | Groww Quotient
mailed-by:	delivery.groww.in
Signed by:	groww.in
'''

# email = re.findall(r"[0-9a-zA-z._+%]+@[0-9a-zA-z._+%]+[.][a-zA-Z.0-9]",str
email = re.findall(r'\w+@\S+\w', str)

# \W IS RETURN A TO Z LETTER AND UNDER SCORE AND 0 TO 9
# \S NOT WHITE SPACE CHAT

print(email)