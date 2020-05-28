function hello () {
    console.log('Hello', this)
}

const person={
    name: 'Vlad',
    age: 25,
    sayhello: hello,
    sayHelloWindow: hello.bind(document),
    logInfo: function (job, phone) {
        console.group(`${this.name} info:`)
        console.log(`Name is ${this.name}`)
        console.log(`Age is ${this.age}`)
        console.log(`Job is ${job}`)
        console.log(`Phone is ${phone}`)
        console.groupEnd()
    }
}

const lena={
    name: 'Elena',
    age: 23
}

// person.logInfo.bind(lena,'Abb','7906333')()
// person.logInfo.call(lena,'Abb','7906333')
// person.logInfo.apply(lena, ['Abb','7906333'])

// let array=new Array()
// array=[1,2,3,4,5]
// const MultBy=(arr,n) => arr.map(i=> i*n)
//
// console.log(MultBy(array,10))
//
// Array.prototype.multBy=function (n) {return MultBy(this, n)}
// console.log(array.multBy(1000))

// function createCalcFunc(n) {
//     return function () {
//         console.log((1000*n))
//                     }
// }
//
// const calc=createCalcFunc(42)
// calc()

// function createIncrementor(n) {
// return function (num) {
//     return n+num
// }
// }
// const addOne=createIncrementor(1)
// const addTen=createIncrementor(10)
// console.log(addOne(10))
// console.log(addOne(50))
// console.log(addTen(50))


// function urlGenerator(domain) {
//  return function (url) {
//         return `https://${url}.${domain}`
//  }
// }
// const comUrl=urlGenerator('com')
// const ruUrl=urlGenerator('ru')
// console.log(comUrl('www.abb'))
// console.log(ruUrl('www.abb'))
//
// function logPerson() {
//     console.log(`Person: ${this.name}, ${this.age}, ${this.job}`)
// }
//
// const person1={name: 'Михаил', age: 22, job: 'Frontend'}
// const person2={name: 'Елена', age: 19, job: 'SMM'}
//
// function bind(context, fn) {fn.call(context)}
//
//
// bind(person1, logPerson)
// bind(person2, logPerson)

// console.log(' Request data ....  ');
// window.setTimeout(()=> {
//     console.log('Preparing data .... ');
//     const backendData={
//     server: 'aws',
//         port: 2000,
//         status: 'working'
//     };
//     setTimeout(()=> {
//         backendData.modified=true;
//         console.log('Data received', backendData)
//     }, 2000);
// }, 5000);
//
// console.log(' end ');

// const p=new Promise(function (resolve, reject) {
// setTimeout(()=>{
//     console.log('Preparing data .... ');
//     const backendData={
//         server: 'aws',
//         port: 2000,
//         status: 'working'
//     };
//     resolve(backendData);
//     }, 3000)
// });
//
// p.then((data)=> {
//     return new Promise((resolve,reject)=> {
//            data.modified=true;
//            resolve(data)
//      }, 2000);
//     })
//     .catch(err=> console.error('Error', err))
//     .then(clientData=>{
//         console.log('Data received', clientData)
//         return clientData})
//     .then((data)=>{
//         setTimeout(console.log(' Modified', data),3000)
//     })
//     .finally(()=> console.log(' Finally'))


// const sleep=ms=> {
//     return new Promise(resolve => {
//         setTimeout(() => resolve(), ms)
//     })
//     };
// // sleep(2000).then(()=> console.log('After 2 seconds'))
// // sleep(2000).then(()=> console.log('After 2 seconds'))
// Promise.all([sleep(2000), sleep(5000)])
// .then(()=> {
//     console.log('All promises')
// })
//
// Promise.race([sleep(2000), sleep(5000)])
//     .then(()=> {
//         console.log('Race promises')
//     })
//
// const p=new Promise((resolve,  reject)=>{
//     console.log(' хаюшки ')
//
//     setTimeout(function(){return resolve(' всё отлично ')}, 5000)
// })
//
// p.then(result=> alert(result), error=> alert(error))

function loadScript(src, callback) {
    let script = document.createElement('script');
    script.src = src;
    //
    script.onload = () => callback()

    script.onerror = () => callback(new Error(`Ошибка загрузки скрипта ${src}`));

    document.head.append(script);
}

loadScript('tests.js', function(sсript) {
    func('Andrew');
    loadScript(' ShortWay.js', function (sсript) {
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
        res=SearchShotWay('A', 'G',ways);
        const minI=res
            .map(i=> i.length)
            .reduce((i, y)  => Math.min(i,y), 1000000);
        const min=res.filter((i)=> i.length=== minI);
        console.log(min);
        alert(' вторая функция ')
    })
})

const but=document.getElementById('test-button')
const inp=document.querySelector('#input-time')

function Samurai(name) {this.name=name}
Samurai.prototype.sayhello=function () {console.log(`${this.name} привет`)
}
vasya=new Samurai ('Вася')
vasya.sayhello()

class NewSamurai {
    constructor(name) {
        this.name = name
    }

    sayhello = function () {
        console.log(`${this.name} привет`)
    }
}
petya= new NewSamurai('Петя')
petya.sayhello();
SuperSamurai= new Function('name', 'this.name=name');
SuperSamurai.prototype.sayhello=function(){
    console.log(`${this.name} привет`)
};

// SuperSamurai.sayhello('John')

obj=new Object( {name: ' Петя',
surname: 'Иванов '})