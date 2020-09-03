import React, {Component} from "react";
import ItemList from "../item-list";
import ItemDetails, {Record} from "../item-details";
import ErrorIndicator from "../error-indicator";
import ErrorBoundry from "../error-boundry";
import SwapService from "../../services/swapi-service";

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




export default class PeoplePage extends Component {

    state={selectedPerson:3, hasError: false};
    swapi=new SwapService()

    onPersonSelected=(id)=> {
        this.setState({selectedPerson:id})
    };

    componentDidCatch()
    { this.setState({hasError: true})}

    render() {
    if (this.state.hasError) {
            return <ErrorIndicator/>}
    const {getPerson, getPlanet, getStarship,getPersonImage, getStarshipImage, getPlanetImage}=this.swapi;
    const itemlist=<ItemList getData={this.props.getData} onItemSelected={this.onPersonSelected}
                             >{this.props.children}</ItemList>
    const personDetails=<ItemDetails itemId={this.state.selectedPerson}
                                         getData={getPerson}
                                         getImageUrl={getPersonImage}>
            <Record field="gender" label="Gender"/>
            <Record field="eyeColor" label="Eye Color"/>
        </ItemDetails>
    return <ErrorBoundry><Row left={itemlist} right={personDetails}/></ErrorBoundry>

}
}