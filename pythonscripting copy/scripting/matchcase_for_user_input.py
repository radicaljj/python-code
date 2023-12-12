

def do_this():
    print("doing this")


def do_that():
    print("doing that")


match input("doing this or that? "):
    case "this":
        do_this()
    case "that":
        do_that()
    case invalid:
        print("Invalid input")
