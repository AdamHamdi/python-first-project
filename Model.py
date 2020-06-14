
import OOPbasicClass
#import a file using this way


def main():
    car=OOPbasicClass.Car()#create an instance from the class Car in the imported file
    car._Name='Alex'
    car.GetOwner()
    car.SetOwner('Adam')
    car.GetOwner()

if __name__ == '__main__':main()