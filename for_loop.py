class for_loop():
    def for_loop(self):
        n=int(input("enter the table"))
        #res=0
        print ("*****************\n")
        for i in range (1,10+1):
            #res= n * i
            print ("{} * {}  =  {}".format(n,i, n*i))
def main():
    loop = for_loop()
    loop.for_loop()
if __name__ == "__main__":
    main()
