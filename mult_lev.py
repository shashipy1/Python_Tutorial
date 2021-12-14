class dad:

     basketball = 11

class son(dad):

    dance = 4
    basketball = 12
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class grandson(son):
    dance = 6
    basketball = 36
    # gitar = 7
    # def isdance(self):
    #     return f"Jackson yeah! " \
    #             f"Yes I dance very awesomely {self.dance} no of times"

darry = dad()
shashi = son()
rahul = grandson()

print(shashi.isdance())
print(rahul.isdance())
print(rahul.basketball)





