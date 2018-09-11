#this program for random.randint(1,20) if clinet choice the number win/
def check():
    guess = input("type a number betwin (1,20):")
    import random
    x = random.randint(1,20)
    z = str(x)
    while guess == z:
        print ("win hoho if you want double win betwin 2 number type a number betwin (1,2):")
        def double():
            print()
            gues = input("type a number:")
            a = random.randint(1,2)
            v = str(a)
            if gues == v:
                print(a)
                print ("nice man big win. lets play again );")
                print()
                return check()
            if gues != v:
                print("lose ):")
                return check()
                cc = input("if you want play more type yes/")
                if cc == 'yes':
                    return check()
            elif gues > 2:
                print("pleaze br carful betwin (1,2);")
                return double()
        double()
    else:
        print("the true number is " , x)
        print("lose try again")
        return check()
check()
