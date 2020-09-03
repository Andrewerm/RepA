import React, {Component} from "react";
import SelectService from "../select-service";
import SelectCity from "../select-city";
import WeatherInform from "../weather-inform";
import OpenWeather from "../weather-services/weather-services";

export default class App extends Component{
    state={weather:null}

    render() {


    const openW = new OpenWeather('4f890b03d18041e7a8bf10e8f660db06', {})
    // openW.getReq().then(resp => this.setState({weather:resp}))
        openW.getReq().then(resp=>console.log(resp))

    return <div><SelectService/>
            <span><SelectCity/>
    <WeatherInform/>
    </span></div>
    }
}
