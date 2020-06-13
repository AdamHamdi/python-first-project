def main():
    #tuple form
    ages=(30,40,15,32,78)
    print(ages,type(ages))
    print(ages[0:5])#thirs item until forth item
    nums=[20,15,65,42,85,12]
    nums.append(120)# ajouter un element dans la liste
    nums.insert(1,55)# inserer 55 dans l'index 1
    print(nums, type(nums))
    print(nums[0:5])#print de l'index 0 jusqu'à n-1
    name="Adam and"
    print(name, type(name))
    

if __name__=='__main__':main()
#apple et executer la fonction main de cette façon