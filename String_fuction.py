def main():
    sentence="Welcome to the first app in paython"
    print('sentence',type(sentence))
    print(len(sentence))
    print (sentence.lower())
    print(sentence.upper())
    print(sentence.split())#diviser le str par rapport les espaces
    print(sentence.split('i'))
    x=sentence.split()
    print(x)
    y=":".join(x)#fusioner les : au lieu de l'espace dans la variable x
    print(y)
    y = " ".join(x)  # fusioner les espaces dans la variable x
    print(y)
    print(sentence.find('first'))#permet de chercher les str
    print(sentence[11])
    print(sentence[15:20])
    a="Adam"
    print('{}'.format(a),'you are {}'.format(sentence))
    #result='Adam' you are 'Welcome to the first app in paython'
if __name__=='__main__':main()
#appele de la fonction main de cette façon

