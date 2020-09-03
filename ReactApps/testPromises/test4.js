const delay=ms=> new Promise(resolve=>setTimeout(()=>resolve(),ms));

// delay(2000).then(txt=>console.log(txt));

const url='https://jsonplaceholder.typicode.com/todos/1';
function fetchTodos() {
    console.log('fetch doto started...');
    // return delay(2000)
    //     .then(()=>{
        return fetch(url)
   }
        .then(response=>response.json())
// }

fetchTodos()
    .then(data=>{
    console.log("data", data)
})
    .catch(e=>console.error(e));

