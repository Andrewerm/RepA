// главный модуль
import WeatherStore  from "./models";
import Render, {WeatherModule} from "./views";
const CHELNY={lat:'55.73', lon:'52.4332'}

// WeatherStore.updateServicesData({lat:'55.73', lon:'52.4332'})
const w=[new WeatherModule('Сервис Weather 2', 'AWeather'), new WeatherModule('Яндекс Погода ', 'YandexWeather'), new WeatherModule('Сервис Weather', 'AWeather'),
    new WeatherModule('Сервис Open Weather Map', 'OpenWeatherMap'),  new WeatherModule('Сервис Dark Sky', 'DarkSky'),
    new WeatherModule('Сервис Open Weather Map 2', 'OpenWeatherMap')]
Render.render(document.getElementById('root'), w)
WeatherStore.subscribe(w)
WeatherStore.run(CHELNY)