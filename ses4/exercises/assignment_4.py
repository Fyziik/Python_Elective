import sys

def greeting(x):
    del x[0]

    if len(x) > 0:
        if x[0] == "-it":
            print("-it flag initiated")
        else:
            print("-it flag required")

        if len(x) > 1:
            if x[1] == "--rm":
                print("--rm flag initiated")
        

greeting(sys.argv)