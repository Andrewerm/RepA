import React, {Component} from "react";
import SelectService from "../select-service";
import SelectCity from "../select-city";
import WeatherInform from "../weather-inform";
import {OpenWeather, DarkSky, Weather} from "../weather-services/weather-services";
export default class App extends Component{
    state={weather:null}

    render() {
    const coordZelen={lat:'55.8466415', lon:'48.5009155'}
    const Api_key='88a0c10e25msh4b3d39a9d6789cbp154f55jsn1bc8f504de0c'
    const darkSkyW = new DarkSky(Api_key)
    darkSkyW.getCurrentTemp(coordZelen).then(resp=>{
       console.log(`${darkSkyW.SERVICE_NAME} ${resp}`)}
        )

    const openW = new OpenWeather(Api_key)
        openW.getCurrentTemp(coordZelen).then(resp=>{
            console.log(`${openW.SERVICE_NAME} ${resp}`)}
        )
    const w = new Weather(Api_key)
        w.getCurrentTemp(coordZelen).then(resp=>{
            console.log(`${w.SERVICE_NAME} ${resp}`)}
        )

    return <div><SelectService/>
            <span><SelectCity/>
    <WeatherInform/>
    </span></div>
    }
}
