def summatorR(ar):
    ar1=ar.copy()
    if len(ar1)==1:
        return ar1[0]
    else:
        res= ar1.pop()+summatorR(ar1)
        return res



def Testing(func):
    def summa(arr):
        sum=0
        for i in arr:
            sum+=i
        return sum
    ar=[1,5,5,10,112,58,25,24,25,65,17,544,655]
    print(ar, func(ar), summa(ar))
    if func(ar)==summa(ar):
        print(' Успешно ')
    else: print(' провал')

Testing(summatorR)
