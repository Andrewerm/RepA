from collections import deque

ways=[('A', 'B'),
      ('B','D'),
      ('A', 'C'),
      ('C', 'F'),
      ('F', 'D'),
      ('D', 'E'),
      ('D', 'G'),
      ('E', 'G'),
      ('A', 'F'),
      ('F','H'),
      ('D','C')
      ]

def SearchShotWay(start, end):
    search_queue=deque()
    store=[]
    routes=[]
    def add_store(elem):
        a=store.get(elem[0])
        if a and elem[1] not in a:
            store[elem[0]].append(elem[1])
        else: store[elem[0]]=[elem[1]]

    for i in ways:
        add_store(i)

    if end in store[start]:
        routes.append(start,end)
        else


SearchShotWay('A', 'G')