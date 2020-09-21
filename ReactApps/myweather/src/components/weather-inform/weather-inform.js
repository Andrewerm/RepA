import React, {Component} from "react";
import {DarkSky, OpenWeather, Weather} from "../weather-services/weather-services";
import SelectService from "../select-service";
import ErrorIndicator from "../error-indicator";

export default class WeatherInform extends Component {
        state={weatherList:[], hasError: false}
        coord={lat:'55.73', lon:'52.4332'}
        api_key='88a0c10e25msh4b3d39a9d6789cbp154f55jsn1bc8f504de0c'

        receiveWeather=(obj)=> {
            obj.getCurrentTemp(this.coord).then(resp=>{
                    const weather={srvName:obj.SERVICE_NAME, current_temp: resp}
                    this.setState((state)=>{
                        let list=state.weatherList
                        list.push(weather)
                        console.log(list)
                        return {weatherList:list}
                    })
                }
            )
    }
    componentDidCatch() {
        this.setState({hasError:true})
    }


    componentDidMount() {
            // const darkSkyW = new DarkSky(this.api_key)
            const openW = new OpenWeather(this.api_key)
            const w = new Weather(this.api_key)
            // this.receiveWeather(darkSkyW)
            this.receiveWeather(openW)
            this.receiveWeather(w)

        }
        render() {
            const {weatherList, hasError}=this.state
            if (hasError) {
                return <ErrorIndicator/>
            }
            const weatherItems=weatherList.map((item)=><li key={item.srvName}> <SelectService wItem={item}/></li>
            )

            return <ul> {weatherItems} </ul>
        }

}

