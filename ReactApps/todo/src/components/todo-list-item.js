import React from "react";

const Todolistitem=( {label, important=false})=> {
    const liStyle={
        color: important? 'tomato' : 'black',
        fontSize: important? '20px' : '10px'
    }
    return <span style={liStyle}> {label} </span>
}

export default Todolistitem