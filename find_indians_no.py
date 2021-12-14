import re

myno = '''hello in this srting is staring with 91 as indain no
+91-2345656784, +91-384749394,+91-3848597,+91-93495523825,0-9394567238, +91-37475,
+91-324I94348'''

patt = re.compile(r'\b{0}-\d{10}')
matches = patt.finditer(myno)
for match in matches:
    print(matches)