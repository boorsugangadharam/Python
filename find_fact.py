class find_fact():
    
    def fact(self):
        n=int(input("enter the factorial number"))
        factorial =1
        #print (n)
        for i in range(1,n+1):
            factorial = factorial * i
        print ("factorial of {} is {}".format(n,factorial) )

def main():
    f= find_fact()
    f.fact()
if __name__ == "__main__":
    main()

    



