function funcA() {
    let a=1
    function funcB() {
        let b=2
        function funC() {
            let c=3
            console.log('funC:', a,b,c)
                 }
        funC()
        console.log('funcB:', a, b)
    }
    funcB()
    console.log('funcA:', a)
}

funcA()