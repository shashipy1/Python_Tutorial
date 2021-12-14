import requests
import pickle
data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/")
# print(data)
l1 = data.split("\n")
print(l1)

l2 = [item.split(",") for item in l1 if len(item)!=0]
# l2 = [item.split(",") for item in data.split("\n") if len(item)!=0]
print(l2)

with open("myiris.pkl","wb") as f:
    pickle.dump(l2, f)



 
# for check file & to read this pikle file use this code
# import pickle
# with open("myiris.pkl", "rb") as f:
#     print(pickle.load(f))