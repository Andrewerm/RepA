import React, {Component} from "react";
import SwapiService from "../../services/swapi-service";
import Spinner from "../spinner";
import ErrorIndicator from "../error-indicator";
import './random-planet.css'

export default class RandomPlanet extends Component {
    swapi=new SwapiService();
    state={planet: {},
    loading: true,
    error: false};

    componentDidMount() {
        this.updatePlanet();
        this.interval=setInterval(()=>this.updatePlanet(), 3000)
    }

    componentWillUnmount() {
        clearInterval(this.interval)
}

    onPlanetLoaded=(data)=>{
        this.setState({loading: false,
        planet:data})
    };

    onError=(err)=>{
        this.setState({error:true,
            loading: false})
    };

    updatePlanet(){
        const id=Math.round(Math.random()*25+2);
        this.swapi
            .getPlanetInfo(id)
            .then(this.onPlanetLoaded)
            .catch(this.onError)
    }


    render() {

        const {planet,loading, error}=this.state;
        const hasData=!(loading||error);
        const errMessage=error?<ErrorIndicator/>:null;
        const spinner=loading?<Spinner/>:null;
        const content=hasData?<PlanetView planet={planet}/>:null;

        return <div>
            <div className="random-planet jumbotron rounded">
                {errMessage}
                {spinner}
                {content}
            </div>
        </div>
    }
}

const PlanetView=({planet})=>{
    const {id, name, populate, rotationPeriod, diameter}=planet;
    return (
        <React.Fragment>
            <img className="planet-image"
                 src={`https://starwars-visualguide.com/assets/img/planets/${id}.jpg`}
                alt='Нет картинки'/>
            <div>
                <h4>{name}</h4>
                <ul className="list-group list-group-flush">
                    <li className="list-group-item">
                        <span className="term">Population: </span>
                        <span>{populate}</span>
                    </li>
                    <li className="list-group-item">
                        <span className="term">Rotation Period: </span>
                        <span>{rotationPeriod}</span>
                    </li>
                    <li className="list-group-item">
                        <span className="term">Diameter: </span>
                        <span>{diameter}</span>
                    </li>
                </ul>
            </div>


        </React.Fragment>
    )}