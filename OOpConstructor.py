
class Car:
    def __init__(self,**kwargs):
        #constructor sera declancher avec toute instance créé
        self.Data=kwargs#lecture de kwargs
    def GetOwner(self):
        print('Owner is ',self.Data["Name"])
        print('Car Model ', self.Data["Model"])
        print('year ', self.Data["Year"])
    def Set_Model(self,Model):
        self.Data['Model']=Model
    def Get_Model(self):
        print('Car Model ', self.Data["Model"])


def main():
    mycar=Car(Name="Adam Hamdi",Model="Camer 2015",Year=2020)
    mycar.GetOwner()
    Gabbycar = Car(Name="Gabriella Daniel",Model="GMC" ,Year=2019)
    Gabbycar.GetOwner()
    #Adam set car_Model
    Gabbycar.Set_Model("Ford Fusion")
    Gabbycar.Get_Model()



if __name__ == '__main__': main()

