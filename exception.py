def main():
    try:
        #out = open("text.txt", "a")  # w=write r=read (a=append=ajouter)
        #out.write("\n name:Adam Hamdi")
        readfile=open("text.txt","r")
        for line in readfile:
            print(line)
        readfile.close()
    except IOError:
        print('file not found')
    else:
      print('operation next')
if __name__=='__main__':main()
#appele de la fonction main de cette façon
