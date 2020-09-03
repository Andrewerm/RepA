import React from "react";
import icon from './starDeath.JPG'
import './error-indicator.css'


const ErrorIndicator=()=>{
    return <div className='error-indicator'>
        <img className='error-image' src={icon} alt='error icon'/>
        <span className='boom'>BOOM!</span>
        <span>что то пошло не так </span>
        <span>(но мы уже послали дроидов решить это)</span>
    </div>
}
export default ErrorIndicator