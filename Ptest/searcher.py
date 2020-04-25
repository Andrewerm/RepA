def SimpleSearch(SearchObject,array):
    i=0
    iter=0
    while i<=len(array)-1:
        iter+=1
        if array[i]==SearchObject: return i+1, iter
        i+=1
    return None, iter


def BinarySearch(SearchObject, array):
    low=0
    high=len(array)-1
    if array[low] == SearchObject: return low + 1, 1
    if SearchObject == array[high]: return high + 1, 2
    iter = 2
    while (high-low)>1:
        iter+=1
        medium=round((high-low)/2)+low
        if SearchObject==array[medium]: return medium+1, iter
        if array[medium]>SearchObject: high=medium
        else: low=medium
    return None,iter


def testing(func):
    arr = (1, 5, 8, 10, 15, 17, 19, 22, 28, 35, 39, 42, 45, 59, 63, 68, 79, 85, 95, 99, 102, 103, 104, 105)
    tests=((42,12), (99, 20), (100, None), (1,1), (68,16), (85,18),(105,24),(69,None))
    for i in range(len(tests)):
        res=func(tests[i][0], arr)
        if res[0]==tests[i][1]:
            print(i+1,'-ый тест успешен, кол-во итераций ', res[1])
        else:
            print(i + 1, '-ый тест провален', res[1])

if __name__ == '__main__':
    testing(SimpleSearch)
    testing(BinarySearch)
