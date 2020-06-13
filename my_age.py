import datetime
def main():
    DOB=input('Enter your age DBO :')#enter your age from the console
    yearNow=datetime.datetime.now().year
    MyAge=yearNow-int(DOB)# int() changer le type de variable
    print('my age is {} years old'.format(MyAge))#print{}+format()



if __name__=='__main__':main()
#appele de la fonction main de cette façon

