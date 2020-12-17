// модуль рендеринга

class Component {
    constructor(name, srvName) {
        this.elem=document.createElement('div');
        // this.elem.id=`id_${name}`;
        this.name=name
        this.srvName=srvName
    }

    renderComponent(parent) {
        parent.append(this.elem)
    }
    updateComponent() {

    }
    }

export class WeatherModule extends Component {
    constructor(name, srvName) {
        super(name, srvName);
        this.elem.className='card';
        this.elem.style="width: 18rem;";
        const header=document.createElement('h5');
        header.class="card-title";
        header.innerHTML=`Сервис: ${name}`;
        this.dataWeather=document.createElement('p');
        this.dataWeather.class="card-text";
        this.dataWeather.innerHTML='инициализация';
        this.elem.append(header);
        this.elem.append(this.dataWeather)
    }
    updateComponent(newdata) {
        this.dataWeather.innerHTML=newdata
        console.info(`Обновили компонент ${this.name}`)
    }
}

//
export default class Render{
    static render (ancor, component) {
        component.forEach(item=>{item.renderComponent(ancor)})
    }

}