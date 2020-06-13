
def main():
    #Key and Value
    #Student={'Name':'Adam Hamdi','Age':28,'Salary':1850}
    Student=dict(Name='Adam Hamdi',Age=28,Salary=1850)
    print(Student,type(Student))
    #Update value
    Student['Name']="Adam HMD"
    #add value
    Student['Dept'] = "Developper"
    print(Student)
    #delete value
    del Student["Dept"]
    print(Student)

if __name__=='__main__':main()
