def main():
    def add(*args):#arg=argument
        total = 0
        for arg in args:
            total += arg
            print (total)

    print (add(1, 2, 5))
    print(add(1, 2, 5,6))
    print(add(1, 2, 5,8))



if __name__=='__main__':main()
#appele de la fonction main de cette façon

