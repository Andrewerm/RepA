const sleep=ms=> new Promise(resolve => setTimeout(()=>{
    resolve(' работает ')},ms))


 sleep(1000).then((txt)=>{console.log(txt)})

// Promise.all([sleep(2000), sleep(6000)])
//     .then(()=>console.log('All promises'))
