import React, {Component} from "react";
import ItemList from "../item-list";
import ItemDetails from "../person-details";
import ErrorIndicator from "../error-indicator";

export default class PageItem extends Component {

    state={selectedPerson:1, hasError:false}

    onSelectedItem=(id)=>{
        this.setState({selectedPerson:id})
    }

    componentDidCatch() {
        this.setState({hasError:true})
    }

    render () {
        if (this.state.hasError) {
            return <ErrorIndicator/>
        }
        const {swapi,labelData}=this.props;
        return <div className="row mb-2">
            <div className="col-md-6">
                <ItemList onSelectedItem={this.onSelectedItem} swapi={swapi} labelData={labelData}/>
            </div>
            <div className="col-md-6">
                <ItemDetails personID={this.state.selectedPerson}/>
            </div>
        </div>
    }
}