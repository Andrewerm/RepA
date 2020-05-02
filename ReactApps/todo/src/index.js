import React from "react";
import ReactDOM from 'react-dom'
import Todolist from './components/todo-list'
import AppHeader from "./components/app-header";
import SearchPanel from "./components/search-panel";

const App=()=> {
    return (
        <div>
            <AppHeader/>
            <SearchPanel/>
            <Todolist/>
        </div>
    )
};

ReactDOM.render(<App/>, document.getElementById('root'));