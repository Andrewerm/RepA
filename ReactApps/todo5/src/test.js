const noPassword=({password, ...rest})=> rest
const user = {
    id: 100,
    name: 'Howard Moon',
    password: 'Password!'
}

console.log(noPassword(user)) //=> { id: 100, name: 'Howard moon' }