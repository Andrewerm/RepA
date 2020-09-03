import React from "react";

const ToogleButton=({action})=> {
    return <button className='btn btn-light' onClick={action}>Вкл/выкл планеты</button>
}

export default ToogleButton