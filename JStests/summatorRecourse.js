function SummatorR(ar) {
    let arr=ar.slice()
    if (arr.length===1) return arr[0]
    else return arr.pop()+SummatorR(arr)

}

function Testing(func) {
    function summa(arr) {
        let sum=0;
        arr.forEach(elem => sum+=elem);
        return sum

    }
    ar=[1,5,5,10,112,58,25,24,25,65,17,544,655];
    console.log(ar+' '+ func(ar)+ ' '+summa(ar) );
    if (func(ar)===summa(ar)) console.log(' тест успешен');
        else console.log(' тест провален')


}


Testing(SummatorR);