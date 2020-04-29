const SearchShotWay=function(start,end) {

    let STORE={}
    let ROUTES=[]
    const add_store=function (elem) {
        if (elem[0] in STORE)
            STORE[elem[0]].push(elem[1])
        else STORE[elem[0]] = [elem[1]]
    }

    const neighbors=function (arr1) {
        return STORE[arr1.slice(-1)]
    }


    const AddRoute=function(routeA) {
        let routeB=[...routeA];
        if (routeB[routeB.length-1]!==end &&
            routeB[routeB.length-1] in STORE){
            directs=neighbors(routeB)
                .filter(x => routeB.indexOf(x)===-1);
            directs.forEach(i=> {
                routeB.push(i);
                AddRoute(routeB);
                routeB.pop()
                })
            }
        else {
            if (routeB[routeB.length-1] === end){
                ROUTES.push(routeB.slice());
                return;

            }
        }


    }




    ways.forEach(i => add_store(i));

    AddRoute([start])
    // minimum= min(list(map(len,ROUTES)))
    // return list (filter(lambda x: len(x)==minimum, ROUTES))
return ROUTES

};





const ways = [['A', 'B'],
    ['B', 'D'],
    ['A', 'C'],
    ['C', 'F'],
    ['F', 'D'],
    ['D', 'E'],
    ['D', 'G'],
    ['E', 'G'],
    ['A', 'F'],
    ['D', 'C'],
    ['F', 'H'],
];
console.log(SearchShotWay('A', 'G'));