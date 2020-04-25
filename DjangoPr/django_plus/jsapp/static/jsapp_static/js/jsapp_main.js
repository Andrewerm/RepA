// var para = document.querySelector('p');
// var book = {
//      topic: 'js',
//     fat: true
// };

//
// book.topic = ' Ура ';
// para.addEventListener('click', updateName);
// book.content= { };



// function updateName() {
//   var name = prompt('Enter a new name');
//   para.textContent = 'Player 1: ' + name;
// }


var myobject = {
    name: 'Рыбалка на',
    method1() {
       alert('озеро')
    },
    method1_1 () {
        alert(this.name)
    }
}

// myobject.method1_1()
// myobject.method1()
// myobject.method2= function () {
//     alert('речка')
// }
// myobject.method2()

let user = {name: 'Вася'};
let admin = {name: 'Петя'}

function says(){
    alert(' меня зовут ' + this.name)
}
user.greetings=says
admin.greetings=says
user.greetings()
admin.greetings()
const newV=user
user=null
newV.greetings()
