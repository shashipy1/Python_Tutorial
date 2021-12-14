# pickle means packed object and important py module

import pickle

# cars = ["audi", "bmm", "Maruti Suzuki", "honda"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()


file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
