def main():
    #creation d'un fichier
    out=open("text.txt","w")#w=write r=read (a=append=ajouter)
    out.write("\n name:Adam Hamdi")#ecrire dans le fichier
    #out.write("\n name:dani")
    out.close#fereture d'un fichier
    readfile=open("text.txt","r")
    for line in readfile:
        print(line)
    readfile.close()
if __name__=='__main__':main()
#appele de la fonction main de cette façon

