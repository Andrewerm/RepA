//  const people=[
//      {name:'Петя', age:25 , budget: 35000},
//      {name:'Вася', age:32 , budget:28000},
//      {name:'Дима', age: 49, budget:12000},
//      {name:'Алмаз', age: 25 , budget:21000},
//      {name:'Андрей', age: 39, budget:71500},
//      {name:'Коля', age: 55 , budget:22500}
//
//  ]
//
//  let newa=people.filter(elem => {
//      if (elem.age>30) return true
//  })
//  console.log(newa)
//  let newarray=people.filter( elem => elem.age>30)
//  console.log(newarray)
//
//  const amount=people.reduce((total,elem)=> total+elem.budget,0)
//  console.log(amount)
//  const mediumAge=people.reduce((med, elem)=> med+elem.age/people.length,0)
//  console.log(mediumAge)
//
//  const Pete=people.findIndex(elem=> elem.name==='Петя')
//  console.log(Pete)
//
//  const highBudget=people
//      .filter(elem => elem.budget> 25000)
//      .map(elem => {
//          return {
//              info: `Имя ${elem.name} (возраст ${elem.age})`,
//              budget: elem.budget
//          }
//      })
//      .reduce((summa, elem) => summa+elem.budget, 0)
//
//  console.log(highBudget)
//
//  const square=(x) => x*x
//
//  const arr=['1', '2', '3', '4', '5', '6', '7', '8']
//  const res=arr
//      .map(elem => parseInt(elem))
//      .filter(elem =>  elem % 2)
//      .reduce((max, elem) =>
//      {if (elem > max) return elem }, 0 );
//
//  console.log(res);
//
//  const greeter={
//      greet: function (name) {console.log(`Hello ${name}`)},
//      greetAll: function (names) {names.forEach(name => this.greet(name))
//               }
//  };
//
//  greeter.greetAll(['Вася','Петя','Дима']);
//
// function f(a,b,...numbers) {
//      console.log(numbers);
//      numbers.forEach(elem =>  console.log(elem))
//  }
//
//  f(1,2,3,4,5,6,7,8)
//
// const arr1=[1,2,3,4,5]
// const arr2=[3,4,3,4,10]
// const res1=Math.max(...arr1, ...arr2)
//  console.log(res1)
// const arr=[...arr1, ...arr2]
// console.log(arr)
//
// const person={
//     firstName: 'Andrew',
//     lastName: 'Ermakov',
//     age: 39
// }
//
// const {firstName, lastName}= person;
// console.log(firstName, lastName)
//
// function  connect({
//     host='1221',
//     port =12345,
//     user= 'admin'
//                   }) {
//     console.log(user, port, host)
// }
//
// connect ({host:5555})
//
// const dict= {
//      duck: 'quack',
//      dog: 'wuff',
//      mouse: 'squeak',
//      hamster: 'squeak',
//  };
//
// const res=Object.entries(dict)
// // const {duck, ...other}=dict
//     .filter(([, value]) => value==='squeak')
//     .map(([key]) => key)
// console.log(...res)

// const shape={
//     type: 'segment',
//     coordinates: {
//         start:[10,15],
//         end: [17,15]
//     }
// }
//
// const {coordinates: {start:[,startY],
//     end: [,endY]}}=shape;
//
// console.log(startY)
//
// const test=`Hello ${Date.now()}, такие координаты`;
// console.log(test)

// const prefix='_blah_'
// const data={
//     [prefix+'name']: 'Bob',
//     [prefix+'age']:23
// };
//
// const defaults={
//     host:' localhost',
//     dbName: 'blog',
//     user: 'admin'
// }
// const opts={
//     user: 'John',
//     password: 'utopia'
// }
//
// const res=Object.assign({}, defaults, opts)
// console.log(res);
// const res2={...defaults,
//     ...opts,
//     port,
//     connect(){}}
//
// console.log((res2))


//
// const dog={
//     name: 'dog',
//     voice: 'woof',
//     }
//
//
// function Animal(name, voice) {
//     this.name=name;
//     this.voice=voice;
//     }
//
// Animal.prototype.say=function () {
//     console.log(`${this.name} goes ${this.voice}`)}
//
//
// const dog=new Animal('dog','voice');
// const cat=new Animal('cat', 'meow');
//
//
// dog.say();
// cat.say();
//
//
function Car1(color, speed, doors){
    this.color=color;
    this.speed=speed;
    this.doors=doors
}
//
// Car.prototype.info=function () {
//     console.log(` Цвет: ${this.color}`)
// }
//
//
// const BMW= new Car('black', 220, 4)
// const Mers=new Car('white', 250, 4)
// console.log(BMW, Mers)
// BMW.info()
// Mers.info()
//

// class Animal{
//     constructor(name, voice) {
//         this.name=name;
//         this.voice=voice
//     }
//     say(){
//         console.log(`${this.name} goes ${this.voice}`)
//     }
// }
//
// class Car {
//     constructor(color, speed, doors) {
//      this.color = color;
//      this.speed=speed;
//      this.doors=doors
//     }
//     info() {console.log(` Цвет: ${this.color}`)}
// }
//
// const dog=new Animal('dog','voice');
// dog.say()
//
// const BMW= new Car('black', 220, 4)
// const Mers=new Car('white', 250, 4)
// console.log(BMW, Mers)
// BMW.info()
// Mers.info()
//
// class Bird extends Animal{
//     constructor(name, voice, canFly) {
//         super(name, voice);
//         this.canFly=canFly
//     }
// say() {
//     super.say();
//     console.log(' Ho ')
// }
// }
//
// const duck= new Bird('Duck', 'quack', true);
// duck.say()


class Counter{
    count=0;
    inc=()=>{
        this.count++;
        console.log(this.count)
    }
}

const cnt=new Counter();
console.log(cnt.count);
cnt.inc();



export {Counter, Car1};





