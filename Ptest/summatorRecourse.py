def summatorR(ar):
    ar1=ar.copy()
    if len(ar1)==1:
        return ar1[0]
    else:
        res= ar1.pop()+summatorR(ar1)
        return res


def maxR(ar):
    ar1=ar.copy()
    if len(ar1)==2:
        return ar1[0] if ar1[0] > ar1[1] else ar1[1]
    else:
        out=ar1.pop()
        max1=maxR(ar1)
        return out if out>max1 else max1





def Testing(func):
    def summa(arr):
        sum=0
        for i in arr:
            sum+=i
        return sum
    ar=[1,5,5,10,112,58,25,24,1545,25,65,17,544,655]
    print(ar, func(ar), summa(ar))
    print(' Успешно ') if func(ar)==summa(ar) else print(' провал')

Testing(summatorR)
print(maxR([1,5,5,10,112,58,25,2004,25,65,17,544,655]))
