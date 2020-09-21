import React, {Component} from "react";
import SelectCity from "../select-city";
import WeatherInform from "../weather-inform";
export default class App extends Component{
    render() {
    return <div><span><SelectCity/>
        <p> Сравним погоду на разных сервисах: </p>
    <WeatherInform/>
    </span></div>
    }
}
