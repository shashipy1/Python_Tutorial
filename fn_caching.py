import time
from functools import lru_cache

@lru_cache(maxsize=33)

def somework(n):
    # some task taking n second
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("now running some work")
    somework(3)
    somework(4)
    somework(6)
    somework(7)
    print("done...........calling again")
    input()  # give one input
    somework(3)
    print("called again")