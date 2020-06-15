



import re#call a regular expression
def main():
    readfile=open("Regfile","r")
    for line in readfile:
        if re.search("(Ad|Sa)(am|ir)",line):
         print(line)
    readfile.close()



if __name__=='__main__':main()


