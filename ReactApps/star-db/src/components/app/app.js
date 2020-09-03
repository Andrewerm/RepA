import React, {Component} from "react";
import Header from "../header";
import RandomPlanet from "../random-planet";
import './app.css'
import ToggleRPButton from "../toggle-rp";
import ErrBatton from "../err-button";
import ErrorIndicator from "../error-indicator";
import PeoplePage from "../people-page";
import SwapService from "../../services/swapi-service";
import ItemDetails, {Record} from "../item-details";
import ErrorBoundry from "../error-boundry";
import CdekApiService from "../../services/cdek-api-service";



const Row=({left, right})=>{
    return <div className="row mb-2">
        <div className="col-md-6">
            {left}
        </div>
        <div className="col-md-6">
            {right}
        </div>
    </div>
};

export default class App extends Component {
    state={toggleRP:true,
    hasError: false};
    swapi=new SwapService()

    toggleButtonClck=()=>{
        this.setState(({toggleRP}) =>{return {toggleRP: !toggleRP}});
     };

    componentDidCatch(error, errorInfo) {
        this.setState({hasError:true})
    }

    render() {
        const {toggleRP}=this.state;
        const toggleRPFrame=toggleRP?<RandomPlanet/>:null;
        if (this.state.hasError) {
            return <ErrorIndicator/>
        }
        const {getPerson, getPlanet, getStarship,getPersonImage, getStarshipImage, getPlanetImage}=this.swapi;
        const personDetails=<ItemDetails itemId={2}
            getData={getPerson}
            getImageUrl={getPersonImage}>
            <Record field="gender" label="Gender"/>
            <Record field="eyeColor" label="Eye Color"/>
            </ItemDetails>
        const planetDetails=<ItemDetails itemId={3}
            getData={getPlanet}
            getImageUrl={getPlanetImage}>
            <Record field="populate" label="Population"/>
            <Record field="diameter" label="Диаметр"/>
        </ItemDetails>;
        const starShipDetails=
            <ItemDetails itemId={2}
            getData={getStarship}
            getImageUrl={getStarshipImage}>

            </ItemDetails>

        return (<div>
            <Header/>
            {/*<ErrorBoundry>*/}
            {/*<Row left={personDetails} right={planetDetails}/>*/}
            {/*</ErrorBoundry>*/}


            {toggleRPFrame}
            <ToggleRPButton onClck={this.toggleButtonClck}/>
            <ErrBatton/>
            <PeoplePage getData={this.swapi.getAllPeople}
            >
            {item=>`${item.name} (${item.gender}, ${item.birthYear}) `}
            </PeoplePage>
            {/*<PeoplePage getData={this.swapi.getPlanets}*/}
            {/*            >{item=>`${item.name} (${item.diameter}) `}</PeoplePage>*/}
            {/*<PeoplePage getData={this.swapi.getStarships}*/}
            {/*>{item=>`${item.name} (${item.model}) `}</PeoplePage>*/}

        </div>)
    }
}
