# show install version

# import sklearn as sk
# print(sk.__version__)


#sys is used to print path

# import sys
# print(sys.path)

# RandomForestClassifier it is a class use in mashine learning
# from sklearn.ensemble import RandomForestClassifier
# print(RandomForestClassifier())

# import file2
# print(file2.a)

# directly import the into the file

from file2 import a,b
print(a,b)

from file3 import a
print(a)

import file4
print(file4.y) # it is batter than file import

import file4
file4.printjoke("funny")