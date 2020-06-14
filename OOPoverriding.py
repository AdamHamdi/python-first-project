


class Operations:
    def Sum(self,n1,n2):
        SumResult=n1+n2
        print('Sum=',SumResult)
    def Sub(self,n1,n2):
        SubResult = n1 - n2
        print('Sub=', SubResult)

        #une deuxième classe
class OperationsWithMul(Operations):#heritage de la classe precedente
    def Mul(self, n1, n2):
        MulResult = n1 * n2
        print('Mul=', MulResult)
    def Sub(self, n1, n2):
       # super().Sub(n1,n2)#appele de la function du class parent
        SubResult = n1-n2*5
        print('Sub=', SubResult)

def main():
   # op1=Operations()
    #op1.Sum(5,6)
    #op1.Sub(15,10)
    opMul=OperationsWithMul()
    opMul.Sum(5, 6)
    opMul.Sub(15, 10)
    opMul.Mul(15, 10)

if __name__ == '__main__':main()



