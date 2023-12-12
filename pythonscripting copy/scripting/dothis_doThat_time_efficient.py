import time
from threading import Thread


def do_this():
    print("starting this!")

    time.sleep(2)
    print("do this")


def do_that():
    print("starting that!")
    time.sleep(3)
    print("did that!")


# do_this()
# do_that()

t1 = Thread(target=do_this)
t1.start()
t2 = Thread(target=do_that)
t2.start()
