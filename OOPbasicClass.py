class Car:
    def SetOwner(self,Name):
        self._Name=Name
    def GetOwner(self):
        print('Owner is ',self._Name)


def main():
    mycar=Car()
    mycar.SetOwner("Adam Hamdi")
    mycar.GetOwner()
    Gabbycar = Car()
    Gabbycar.SetOwner("Gabriella Daniel")
    Gabbycar.GetOwner()



if __name__ == '__main__': main()

