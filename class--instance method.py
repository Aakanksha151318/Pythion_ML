class Demo:
    value = 0
    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2
    def Fun(self):
        print(self.no1,self.no2)

    def Gun(self):
        print(self.no1,self.no2)
def main():
    obj = Demo(11,12)
    obj2= Demo(10,15)
    obj.Fun()
    obj2.Gun()
    obj.Fun()
    obj2.Gun()
if __name__=="__main__":
    main()



