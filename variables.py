def main():
    #int(x) changer le type de x to int
    num=int(30/5)
    print(num, type(num))
    Name="my name is Adam"
    print(Name,type(Name))
    Amount=50# amount of time spend on working
    #{} ==> appele pour quelque chose
    #format(x) met la valeur de x dans une autre valeur
    data="{} is high".format(Amount)
    #data="%s is high"%Amount remplace la ligne precedente mais il est dibriqué
    print(data, type(data))
    dataln='is good'
    print(len(dataln))# len retourne la longueur d'un string
    print(dataln[3])# le resultat est ="g"


if __name__=='__main__':main()
