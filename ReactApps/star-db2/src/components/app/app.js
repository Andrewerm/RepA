import React, {Component} from "react";
import Header from "../header";
import RandomPlanet from "../random-planet";
import ToogleButton from "../toogle-button";
import PageItem from "../page-item/page-item";
import SwapiService from "../../services/swapi-service";
import ErrorBoundry from "../error-boundry/error-boundry";
import ItemDetails from "../person-details";
import {Record} from "../person-details/item-details";

const Row=({left, right})=> {
    return <div className="row mb-2">
        <div className="col-md-6">
            {left}
        </div>
        <div className="col-md-6">
            {right}
        </div>
    </div>

}


export default class Apps extends Component {
    state={
    randomPlanets: true};
    swapi = new SwapiService();

    onClckToogleRandomPlanets=()=>{
        this.setState(({randomPlanets}) => {
                return {randomPlanets:!randomPlanets}
            }
        )
    };

    render() {
        // const randomPlanet=this.state.randomPlanets?<RandomPlanet/>:null;
        const {getPlanetImage, getPersonImage, getStarshipImage, getPerson, getPlanetInfo}=this.swapi;
        const personDetails=<ItemDetails itemID={2}
                                         getImageURL={getPersonImage} getData={getPerson}>
            <Record field="gender" label="Gender"/>
            <Record field="eyeColor" label="Eye Color"/>
        </ItemDetails>
        const planetDetails=<ItemDetails itemID={3}
                                         getImageURL={getPlanetImage} getData={getPlanetInfo}>
            <Record field="populate" label="Население: "/>
            <Record field="diameter" label="Диаметр: "/>
        </ItemDetails>
        return <div>
            <Header/>
            <ErrorBoundry>
                <Row
                right={personDetails}
                left={planetDetails}/>
            </ErrorBoundry>
            {/*{randomPlanet}*/}
            {/*<ToogleButton action={this.onClckToogleRandomPlanets}/>*/}
            {/*<PageItem swapi={swapiService.getAllPeople} labelData={item=>`${item.name} (${item.gender}, ${item.birthYear})`}/>*/}
            {/*<PageItem swapi={swapiService.getPlanets} labelData={item=>`${item.name} (${item.diameter}, ${item.populate})`}/>*/}
            {/*<PageItem swapi={swapiService.getAllShips} labelData={item=>`${item.name} (${item.model}, ${item.manufacturer})`}/>*/}


        </div>
    }
}