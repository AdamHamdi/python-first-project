
def main():
    Age= input('Enter your age :')
    if((int(Age)>=8)and (int(Age)<=10)):
        print('Children')
    elif ((int(Age) >= 11) and (int(Age) <= 15)):
        print('Kids')
    elif ((int(Age) >=16) & (int(Age) <= 18)):
        print('Teenager')
    elif ((int(Age) >=19) & (int(Age) <= 30)):
        print('Young')
    else:
        print('Out of range')
    print('application is ended')





if __name__=='__main__':main()
#appele de la fonction main de cette façon

