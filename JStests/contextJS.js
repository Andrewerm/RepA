// const person= {
//     surname: 'Stark',
//     knows: function (what, name) {
//         console.log(`You ${what} know, ${name} ${this.surname}`)
//
//     }
//
// }
// const john={surname: 'Snow'}
// person.knows(' all', 'Bran')
//
// person.knows.bind(john)('nothing', 'John')

// function Person(name, age) {
//     this.name=name
//     this.age=age
//     console.log(this)
//
// }

// // const elena= new Person('Elena', 20)
// function logThis() {
//     console.log(this)
//
// }
//
// const obj={num:42}
// logThis.apply(obj)
//
// const animal={
//     legs: 4,
//     logThis: function () {
//         console.log(this)
//
//     }
// }
//
// animal.logThis()

function Cat(color) {
    this.color=color
    console.log('This', this);
    (()=> console.log ('Arrow this', this))()

}
new Cat('red')