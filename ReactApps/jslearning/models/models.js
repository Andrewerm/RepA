// модуль с моделями
import {YandexWeather, Weather, OpenWeather, DarkSky} from '../weather-services';
const api_key='88a0c10e25msh4b3d39a9d6789cbp154f55jsn1bc8f504de0c'
const API_KEY_YANDEX='0d859f58-bafe-4bcd-a29a-1dbd1a510ede'
export const SERVICES=[new Weather(api_key), new OpenWeather(api_key), new DarkSky(api_key), new YandexWeather(API_KEY_YANDEX)]

export default class WeatherStore {

    static updateServicesData () {
        SERVICES.forEach(async item=>{
            const res=await item.getCurrentTemp(this.coord);
            const srvname=item.SERVICE_NAME;
            localStorage.setItem(srvname,res);
            //  работа с событиями по обновлению данных
            let events=JSON.parse(localStorage.getItem('events' ))
            if (events) {
                const eventsS=new Set(events)
                eventsS.add(srvname)
                events=[...eventsS]}
            else {events=[srvname]}
            localStorage.setItem('events', JSON.stringify(events))
        })
            }

    static subscribe (listOfModules) {
        if (!this.subscribers) {this.subscribers = {}}
        listOfModules.forEach((item, index)=>{
            // item.updateComponent(`элемент номер ${index} сервис ${item.srvName}`)
            this.subscribers[item.name]=item
        })
    }
    static run(coord){
        this.coord=coord;
        const a=new Promise((resolve)=>{
        this.updateServicesData()
        resolve()});
        const events=JSON.parse(localStorage.getItem('events' ));
        if (this.subscribers) {
            for (let item in this.subscribers)
            {
                console.log(`процесс ${item} начался`);
                a.then(()=>{
                    const tempData=localStorage.getItem(this.subscribers[item].srvName)
                    // debugger;
                    this.subscribers[item].updateComponent(tempData)
                    console.error(`процесс ${item} закончился`);

                })
            }
        }
    }

}



