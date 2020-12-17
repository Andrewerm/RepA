class WeatherServices {
    BASE_URL=null;
    requestOptions=null;
    CORS_URL='https://cors-anywhere.herokuapp.com/'

    constructor(api_key) {
        this.api_key=api_key
        }

    async getReq (params) {
        const url=`${this.BASE_URL}${params}`;
        try{
            const res=await fetch(url, this.requestOptions);
            return await res.json()
        }
        catch(err){
            console.error(`Произошла ошибка ${err}`)
            return {'error': err}
        }
    }
}

export class DarkSky extends WeatherServices {
    METHOD='GET';
    RAPIDAPI='dark-sky.p.rapidapi.com';
    SERVICE_NAME='DarkSky';
    constructor(...args) {
        super(...args);
        this.BASE_URL=`https://${this.RAPIDAPI}`;
        this.requestOptions = requestOptions(this.api_key, this.RAPIDAPI, this.METHOD)
    }

    async getCurrentWeather(coord) {
        const params = `/${coord.lat},${coord.lon}?lang=en&units=auto`;
        const res = await this.getReq(params);
        if (res.error) {return res.error}
        else {return res.currently}

    }
    async getCurrentTemp(coord) {
            const res=await this.getCurrentWeather(coord);
            return res.apparentTemperature
        }
    }


export class OpenWeather extends WeatherServices {
    METHOD='GET';
    RAPIDAPI='community-open-weather-map.p.rapidapi.com';
    SERVICE_NAME='OpenWeatherMap';
    constructor(...args) {
        super(...args);
        this.BASE_URL=`https://${this.RAPIDAPI}/weather`;
        this.requestOptions = requestOptions(this.api_key, this.RAPIDAPI, this.METHOD)
    }

    async getCurrentWeather(coord) {
        const params = `?lat=${coord.lat}&lon=${coord.lon}&lang=ru&units=metric`;
        const res = await this.getReq(params);
        return res.main
    }
    async getCurrentTemp(coord) {
        const res=await this.getCurrentWeather(coord);
        try {
            return res.temp
        }
        catch (e) {
            console.error(`Произошла ошибка ${e}`)
        }
    }
}

export class Weather extends WeatherServices {
    METHOD='GET';
    RAPIDAPI='weatherbit-v1-mashape.p.rapidapi.com';
    SERVICE_NAME='AWeather';
    constructor(...args) {
        super(...args);
        this.BASE_URL=`https://${this.RAPIDAPI}/current`;
        this.requestOptions = requestOptions(this.api_key, this.RAPIDAPI, this.METHOD)
    }

    async getCurrentWeather(coord) {
        const params = `?lat=${coord.lat}&lon=${coord.lon}&lang=en&units=M`;
        const res = await this.getReq(params);
        return res.data[0]
    }
    async getCurrentTemp(coord) {
        const res=await this.getCurrentWeather(coord);
        try {
            return res.temp
        }
        catch (e) {
            console.error(`Произошла ошибка ${e}`)
        }
    }
}


export class YandexWeather extends WeatherServices {
    METHOD='GET';
    YANDEX_URL=`https://api.weather.yandex.ru/v2/informers`
    SERVICE_NAME='YandexWeather';

    constructor(...args) {
        super(...args);
        this.BASE_URL=this.CORS_URL+this.YANDEX_URL;
        this.requestOptions = {headers:{'X-Yandex-API-Key':this.api_key}, method:this.METHOD}
    }

    async getCurrentWeather(coord) {
        const params = `?lat=${coord.lat}&lon=${coord.lon}&lang=ru_RU`;
        return await this.getReq(params);
    }
    async getCurrentTemp(coord) {
        const res=await this.getCurrentWeather(coord);
        try {
            return res.fact.temp
        }
        catch (e) {
            console.error(`Произошла ошибка ${e}`)
        }
    }
}

function requestOptions(apikey, RAPIDAPI, method) {
    const myHeaders = new Headers();
    myHeaders.append("X-RapidAPI-Key", apikey);
    myHeaders.append("x-rapidapi-host", RAPIDAPI);
    return {
        method: method,
        headers: myHeaders
    };
}