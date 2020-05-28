
// let inp=document.createElement('input');
// inp.classList.add('form-control');
// inp.id='price';
// inp.type='number';
// document.querySelector('body').appendChild(inp);
//
// const mas=[['АИ-92', 35], ['АИ-95', 40], ['АИ-98', 45]];
// let but=[];
// let div=[];
// let lab=[];
//
//
// mas.forEach((value, index) => {
//     lab[index]= document.createElement('label');
//     lab[index].innerHTML=`Цена: ${value[1]}`;
//     but[index] = document.createElement('button');
//     but[index].id = index;
//     but[index].classList.add('btn', 'btn-primary');
//     but[index].innerHTML = value[0];
//     but[index].onclick=()=> {
//         let v;
//         if (document.querySelector('input#price').value>0) v = parseInt(document.querySelector('input#price').value);
//             else v=0;
//         sum = v * mas[index][1];
//         document.querySelector('p#sum').innerHTML = ` Стоимость: ${sum}`;
//     };
//     div[index]= document.createElement('div');
//     div[index].id=`id${index}`;
//     document.querySelector('body').appendChild(div[index]);
//     document.querySelector(`div#id${index}`).appendChild(but[index]);
//     document.querySelector(`div#id${index}`).appendChild(lab[index]);
//
// });
// output=document.createElement('p');
// output.id='sum';
// output.innerHTML=' Стоимость: ';
// document.querySelector('body').appendChild(output);

document.querySelector('.one').onclick=(event)=> {
    console.log(event);
    console.log('click')
};
 document.querySelector('.two').onclick=()=> {
     console.log('click2')
 };
document.querySelector('.two').ondblclick=()=> {
     console.log('double')
};

document.querySelector('.two').oncontextmenu=()=> {
         console.log('right button')
    return false
};
// let w=75
// document.querySelector('.three').onmousemove=()=> {
//     document.querySelector('.three').style.width=w+'px';
//     w++
// }

document.querySelector('.three').onmouseenter=()=> {
    document.querySelector('.three').style.background='red';
}

document.querySelector('.three').onmouseleave=()=> {
    document.querySelector('.three').style.background='green';
}

document.querySelector('.three').onmousedown=()=> {
    document.querySelector('.three').style.background='orange';
}


const func=(name)=> {
    alert (`${name}, работает !!!!`)
}

// const xhttp=new XMLHttpRequest()
// xhttp.onreadystatechange=()=> {
//     if (this.readyState==4 && this.this.status==200) myFunction (this.responseText)
// };
//
// const myFunction=(data)=> console.log(data)
//
// const url='http://getpost.itgid.info/index2.php'
// xhttp.open("GET", url, true)
// xhttp.send()
//
// fetch(url)
//     .then(data=>{
//         console.log(data)
//     })

// let promise = fetch(url)
// console.log(promise)
//
// // Данные для передачи на сервер допустим id товаров и его количество
//
// // Создаём объект класса XMLHttpRequest
// const request = new XMLHttpRequest();
//
// /*  Составляем строку запроса и кладем данные, строка состоит из:
// пути до файла обработчика ? имя в GET запросе где будет лежать значение запроса id_product и
// через & мы передаем количество qty_product. */
// const url = "https://api.weather.yandex.ru/v1/informers";
//
// request.withCredentials = true;
//
// /* Здесь мы указываем параметры соединения с сервером, т.е. мы указываем метод соединения GET,
// а после запятой мы указываем путь к файлу на сервере который будет обрабатывать наш запрос. */
// request.open('GET', url);
//
// // Указываем заголовки для сервера, говорим что тип данных, - контент который мы хотим получить должен быть не закодирован.
// request.setRequestHeader('Content-type', 'text/plain', 'X-Yandex-API-Key: ae46126c-27e7-419c-a44c-c503864debe8')
//
// // Здесь мы получаем ответ от сервера на запрос, лучше сказать ждем ответ от сервера
// request.addEventListener("readystatechange", () => {
//
//     /*   request.readyState - возвращает текущее состояние объекта XHR(XMLHttpRequest) объекта,
//     бывает 4 состояния 4-е состояние запроса - операция полностью завершена, пришел ответ от сервера,
//     вот то что нам нужно request.status это статус ответа,
//     нам нужен код 200 это нормальный ответ сервера, 401 файл не найден, 500 сервер дал ошибку и прочее...   */
//     if (request.readyState === 4) {
//
//         // выводим в консоль то что ответил сервер
//         console.log( request.responseText );
//     }
// });
//
// // Выполняем запрос
// request.send();

// xhr.open("GET", "http://127.0.0.1:5000/api/users", true);
// xhr.setRequestHeader("authorization", "Token xxxxxx");
// xhr.setRequestHeader("Version", "1");
// xhr.send();
// xhr.responseText