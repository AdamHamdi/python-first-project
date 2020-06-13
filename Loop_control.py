def main():

    print("starting program ")
    word='python'
    for letter in word:
        #print (letter)
        if(letter=='t'):
            #break leave directly
            continue # continue without printing the letter 't'
        print(letter)



    print("ending program")
if __name__=='__main__':main()


