# Coroutines In Python

def searcher():
    import time
    # some 4 seconds time consumming task
    book = "in this book is associate to all devotees of shrila prabhupada"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
             print("your text is in the book")
        else:
             print("your text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("associate")th
input("press any key")
search.send("shrila prabhupada")
search.send("shashi")
search.close()


# search.send("shrila prabhupada") error --> StopIteration b/c file is close