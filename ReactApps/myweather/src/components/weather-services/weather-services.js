class WeatherServices {
    BASE_URL=null;
    requestOptions=null;


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
        return res.currently

    }
    async getCurrentTemp(coord) {
            const res=await this.getCurrentWeather(coord);
            return res.apparentTemperature
        }
    }


export class OpenWeather extends WeatherServices {
    METHOD='GET';
    RAPIDAPI='community-open-weather-map.p.rapidapi.com';
    SERVICE_NAME='Open Weather Map';
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
    SERVICE_NAME='Weather';
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

function requestOptions(apikey, RAPIDAPI, method) {
    const myHeaders = new Headers();
    myHeaders.append("X-RapidAPI-Key", apikey);
    myHeaders.append("x-rapidapi-host", RAPIDAPI);
    return {
        method: method,
        headers: myHeaders
    };
}