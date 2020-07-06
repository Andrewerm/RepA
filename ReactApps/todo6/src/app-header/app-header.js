import React from "react";
import './app-header.css'

const Appheader=({toDo,done})=> {
    return <div className='app-header d-flex'>
        <h1>My ToDO List</h1>
        <h2>{toDo} to do, {done} done</h2>
    </div>
};

export default Appheader