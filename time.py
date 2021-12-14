
# know time AND sleep is wait time in second then print after few second

import  time
localtime = time.asctime(time.localtime(time.time()))
time.sleep(2)
print(localtime)

# find time
import time
initial = time.time()
# print(initial) time return in mili second
k = 2
while(k<5):
    print("shashi bhai coding achhe se kro")
    time.sleep(2)
    k+=1
print("while loop ran in",time.time-initial,"second")
initial2 = time.time()
for i in range(3):
    print("kya shashi bhai or sb bathiya")
    time.sleep(2) 
print("for loop ran in",time.time-initial2,"second")

