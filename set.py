s = set()
s.add(1)
s.add(3)
s.add(4)
s1=s.union({1,2,3,4})
s2=s.intersection({9,2,6,7})
print(s,s1)
print(s,s2)