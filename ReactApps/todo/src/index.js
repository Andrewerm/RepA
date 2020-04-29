import React from "react";
import ReactDOM from 'react-dom'
// import Todolist from './todolist'


 const Todolist=()=> {
    const items=['Learn React', 'Build Awesome App']


    return(
        <ul>

            <li>{items[0]}</li>
            <li>{items[1]}</li>
        </ul>
    )
}

const AppHeader=()=> {
    return <h1> My ToDo list </h1>
}

const SearchPanel=()=> {
    const searchText='search'
    const searchStyle={
        fontSize: '25px'
    }
    return <input
        style={searchStyle}
        placeholder={searchText}/>

}

const App=()=> {
    return (
        <div>
            <AppHeader/>

            <SearchPanel/>
            <Todolist/>
        </div>
    )
}

ReactDOM.render(<App/>, document.getElementById('root'))