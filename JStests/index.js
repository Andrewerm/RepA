const SimpleSearch=function (SearchObject,arr) {
    let iter=0;
    while (iter<=arr.length-1) {
        if (arr[iter]===SearchObject) return [iter+1,iter+1];
        iter++
    }
    return [null,iter+1]
};

const BinarySearch=function (SearchObject,arr) {
    let low=0;
    let high=arr.length;
    if (SearchObject===arr[low]) return [low+1, 1];
    if (SearchObject===arr[high]) return [high+1, 2];
    let iter=2;
    while (high-low>1) {
        iter++;
        let medium=Math.round((high-low)/2+low);
        if (SearchObject===arr[medium]) return [medium+1, iter];
        if (arr[medium]>SearchObject) high=medium;
            else low=medium
    }
    return [null, iter]

};

const testing=function(func) {
    debugger;
    const arr = [1, 5, 8, 10, 15, 17, 19, 22, 28, 35, 39, 42, 45, 59, 63, 68, 79, 85, 95, 99, 102, 103, 104, 105];
    const tests=[[42,12], [99, 20], [100, null], [1,1], [68,16], [85,18],[105,24],[69,null]];
    tests.forEach((elem,index) => {
        res=func(elem[0],arr);
        if (res[0]===elem[1]) console.log(index+1+' -ый тест успешен, кол-во итераций '+res[1]);
            else console.log(index+1+' -ый тест провален, кол-во итераций '+res[1]);
            }
        )
};


testing(SimpleSearch);
testing(BinarySearch);
