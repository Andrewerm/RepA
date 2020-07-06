import React from "react";
import TodoListItem from "../todo-list-item";
import './todo-list.css'

const TodoList=({todos, deleteClck, toggle})=> {
    const elements=todos.map(item=>{
        const {id, ...restItems}=item;
        return <li key={id} className='list-group-item'>
            <TodoListItem items={restItems}
                          deleteClck={()=>deleteClck(id)} action={(prop)=>toggle(id,prop)}/></li>});
    return (<div>
        <ul>
        {elements}
        </ul>
    </div>)

};
export default TodoList