from functools import reduce

ways=[('A', 'B'),
      ('B','D'),
      ('A', 'C'),
      ('C', 'F'),
      ('F', 'D'),
      ('D', 'E'),
      ('D', 'G'),
      ('E', 'G'),
      ('A', 'F'),
      ('D','C'),
      ('F','H'),
      ]

def SearchShotWay(start, end):
    STORE={}
    ROUTES=[]
    def add_store(elem):
        a=STORE.get(elem[0])
        if a and elem[1] not in a:
            STORE[elem[0]].append(elem[1])
        else: STORE[elem[0]]=[elem[1]]

    def AddRoute(routeA):
        routeB=routeA.copy()
        if routeB[-1]!=end and STORE.get(routeB[-1]):
            arrows=list(filter(lambda x:  x not in routeB, STORE[(routeB[-1])]))
            for i in arrows:
                routeB.append(i)
                AddRoute(routeB)
                routeB=routeB[:-1]
        else:
            if routeB[-1]==end: ROUTES.append(routeB.copy())
            return



    # route=[start]
    for i in ways:
        add_store(i)
    AddRoute([start])
    lenRoutes=list(map(len,ROUTES))
    mini=min(lenRoutes)
    print(list (filter(lambda x: len(ROUTES)==mini , ROUTES)))





SearchShotWay('A', 'E')