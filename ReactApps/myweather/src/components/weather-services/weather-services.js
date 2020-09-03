export default class WeatherServices {
 
    // BASE_URL='https://api.openweathermap.org/data/2.5/onecall?lat=55.743553&lon=52.395820&appid=4f890b03d18041e7a8bf10e8f660db06'
    BASE_URL='https://dark-sky.p.rapidapi.com/55.743553,52.395820'
    constructor(api_key, params) {
        this.params=params
        this.api_key=api_key
        }

    async getReq () {
        var myHeaders = new Headers();
        myHeaders.append("X-RapidAPI-Key", "88a0c10e25msh4b3d39a9d6789cbp154f55jsn1bc8f504de0c");
        myHeaders.append("x-rapidapi-host", "dark-sky.p.rapidapi.com");
        // myHeaders.append("useQueryString", true);

        var requestOptions = {
            method: 'GET',
            headers: myHeaders
        };

        const url=`${this.BASE_URL}`
        const res=await fetch(url, requestOptions)
        const res2=await res.json()
        console.log(res2);
        return res2

    }


}

// export default class OpenWeather extends WeatherServices {
//
// }

