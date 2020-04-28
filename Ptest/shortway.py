
def SearchShotWay(start, end):
    STORE={}
    ROUTES=[]
    def add_store(elem):
        if STORE.get(elem[0]):
            STORE[elem[0]].append(elem[1])
        else: STORE[elem[0]]=[elem[1]]

    def neighbors(arr1):
        return STORE[arr1[-1]]


    def AddRoute(routeA):
        routeB=routeA.copy()
        if routeB[-1]!=end and STORE.get(routeB[-1]):
            directs=list(filter(lambda x:  x not in routeB, neighbors(routeB)))
            for i in directs:
                routeB.append(i)
                AddRoute(routeB)
                routeB=routeB[:-1]
        else:
            if routeB[-1]==end: ROUTES.append(routeB.copy())


    for i in ways:
        add_store(i)
    AddRoute([start])
    minimum= min(list(map(len,ROUTES)))
    return list (filter(lambda x: len(x)==minimum, ROUTES))

if __name__ == '__main__':
    ways = [('A', 'B'),
            ('B', 'D'),
            ('A', 'C'),
            ('C', 'F'),
            ('F', 'D'),
            ('D', 'E'),
            ('D', 'G'),
            ('E', 'G'),
            ('A', 'F'),
            ('D', 'C'),
            ('F', 'H'),
            ]
    print(SearchShotWay('A', 'G'))