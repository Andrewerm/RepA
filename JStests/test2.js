// типы данных
// null примитив
// undefined примитив
// boolean примитив
// number примитив
// string примитив
// object НЕ примитив
// symbol примитив
console.log(typeof 0)
console.log(typeof true)
console.log(typeof 'JS')
console.log(typeof undefined)
console.log(typeof Math)
console.log(typeof Symbol('JS'))
console.log(typeof null)  // неточность
console.log(function() {}) // неточность
console.log(NaN) // неточность

//приведение типов
console.log(Boolean('hello')); // true
console.log(Boolean('')); // false

// Строки и числа
console.log(1+'2') // 12
console.log(1+2) // 3
console.log('1'+'2') // 12
console.log(1+2+'0') // 30
console.log('3'*'8') // 24

// ==vs===
// ==сравнивает без типов данных ;  === с типами данных
console.log(2=='2') // true потому что приводит к одному типу
console.log(2==='2') // false типы разные
console.log(undefined==null) //true
console.log(undefined===null) // false
console.log('0'==false) // true
console.log('1'==true) // true