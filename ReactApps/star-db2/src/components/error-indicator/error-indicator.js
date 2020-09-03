import React from "react";
import icon from './starDeath.JPG'


const ErrorIndicator=()=>{
    return <div className='error-indicator'>
        <img src={icon} alt='error icon'/>
        <span className='boom'>BOOM!</span>
        <span>что то пошло не так</span>
        <span>(но мы уже послали дроидов решить это)</span>
    </div>
}
export default ErrorIndicator