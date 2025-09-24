def timeDecorator(arg):
    def inner(LL,UL):
        import time
        IT = time.time()
        arg(LL,UL)
        FT = time.time()
        print(FT - IT)
    return inner

@timeDecorator
def primeNum(LL,UL):
    for n in range(LL,UL+1):
        if n > 1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                print(n)
primeNum(1,100)