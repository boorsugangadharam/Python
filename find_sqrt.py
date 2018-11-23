class find_sqrt():
    def find_sqrt(self):
        n=int(input("enter the number"))
        half =int(n/2)
        for i in range(1,half+1):
            try:
                if i*i == n:
                    print ("perfect square")
                    exit
                else:
                    pass
            except:
                print("not perfect square")
        

def main():
    sqrt =find_sqrt()
    sqrt.find_sqrt()
if __name__ == "__main__":
    main()
