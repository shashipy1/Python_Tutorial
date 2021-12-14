f1 = open("skk.txt")

try:
    # f = open("dose.txt")
    f= open("dose1.txt") #b/c this file is not presend

# except Exception as e:
#     print(e)
except EOFError as e:
    print("eof error aa gya ", e)

except IOError as e:
    print("IO eof error aa gya ", e)

else:
    print("This will run only if except is not running")
finally:
    print("Run this anyway...........")
    # f.close()
    f1.close()
    print("important stuff")