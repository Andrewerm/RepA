import React from 'react'
import AppHeader from "../app-header";
import TodoList from "../todo-list";
import SearchPanel from "../search-panel";
import ItemStatusFilter from '../item-status-filter'



const App=()=> {
    const todosData= [
        {label: 'Drink Coffee', important: false, id: 1},
        {label: 'Have a lunch', important: true, id: 2},
        {label: 'Build App', important: false, id: 3},
    ];
    return (
        <div>
            <AppHeader/>
            <SearchPanel/>
            <ItemStatusFilter/>
            <TodoList todos={todosData}/>
        </div>
    )
};

export default App