function createFrameworkManager() {
    const fw=['Angular', 'React']
    return {
        print: function () {
            console.log(fw)
        },
        add: function (framework) {
            fw.push(framework)
        }
    }
}

const manager=createFrameworkManager()
manager.print()
manager.add('ViewJS')
manager.print()

const fib=[1,2,3,5,8,13]
for (var i=0; i<fib.length; i++) {
    (function (j){
    setTimeout(function () {
        console.log(`fib${i}=${fib[j]}`)
    }, 1500)
    })(i)
}
