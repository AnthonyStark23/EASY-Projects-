import random
def emojidice(n):
    if(n==1):
        n="\U0001F600"
    elif(n==2):
        n="\U0001F929"
    elif(n==3):
        n="\U0001F60D"
    elif(n==4):
        n="\U0001F970"
    elif(n==5):
        n="\U0001F602"
    x = "y"
    while x == "y":
        no = random.randint(1,6)
        if no == 1:
            print("[--------]")
            print("[        ]")
            print("[   "+n+"   ]")
            print("[        ]")
            print("[--------]")
        if no == 2:
            print("[-----]")
            print("["+n+"   ]")
            print("[     ]")
            print("[   "+n+"]")
            print("[-----]")
        if no == 3:
            print("[--------]")
            print("[        ]")
            print("["+n+" "+n+" "+n+"]")
            print("[        ]")
            print("[--------]")
        if no == 4:
            print("[-------]")
            print("["+n+"   "+n+"]")
            print("[       ]")
            print("["+n+"   "+n+"]")
            print("[-------]")
        if no == 5:
            print("[---------]")
            print("["+n+"    "+n+" ]")
            print("[   "+n+"    ]")
            print("["+n+"    "+n+" ]")
            print("[---------]")
        if no == 6:
            print("[---------]")
            print("["+n+" "+n+" "+n+" ]")
            print("[         ]")
            print("["+n+" "+n+" "+n+" ]")
            print("[---------]")
        x=input("press y to roll again and n to exit:")
        print("\n")
p= random.randint(1,5)
emojidice(p)
