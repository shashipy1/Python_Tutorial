import re

google = ''' Google LLC is an American multinational technology company that specializes in Internet-related 
services and products, which include online advertising technologies, a search engine, cloud computing, 
software, and hardware. Wikipedia
no 34523-1234, 24355-1234,23424-223,2424-24
CEO: Sundar Pichai (2 Oct 2015–)
Founded: 4 September 1998, Menlo Park, California, United States
Headquarters: Mountain View, California,lele United States
Revenue: 18,169 crores USD (2020)
Subsidiaries: YouTube, Fitbit,lele, Firebase, Googleeeeeeee AdMob, Kaggle, MORE
Founders: Larry Page, Sergey Brin
Parent organization: Alphabet Inc.'''

# print(r"\n")
# patt = re.compile(r'fass')---------->only one object print who fass
# patt = re.compile(r'.')------------> all character
# patt = re.compile(r'.Goo')----------------> any charater start
# patt = re.compile(r'^Google')------------>start too Google
# patt = re.compile(r'$Google')------------------>is string end with this character
# patt = re.compile(r'Inc$')-------------------->string end with charater this Inc
# patt = re.compile(r'le*')-------------->more than character
# patt = re.compile(r'l*e*')
# patt = re.compile(r'le+')
# patt = re.compile(r'le{2}') ---------------> two time e as like lee........
# patt = re.compile(r'(le){2}')#--------------------->it measn lele
# patt = re.compile(r'le{1}|g')---------------------->either or means one


# special sequences
# patt = re.compile(r'\AGoogle')------------>starting with Google then return
# patt = re.compile(r'\bGoogle')--------------->starting with googel
# patt = re.compile(r'Google\b')-------------->ending with google
# patt = re.compile(r'4\b')
patt = re.compile(r'\d{5}-\d{4}')
patt = re.compile(r'\d{5}-\d{2}')


matches = patt.finditer(google)
for match in matches:
    print(match)
    # print(google[559:560])