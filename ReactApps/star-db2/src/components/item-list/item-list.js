import React, {Component} from "react";
import SwapiService from "../../services/swapi-service";

export default class ItemList extends Component {
    swapiService = new SwapiService();
    state = {
        peopleList: null
    };

    componentDidMount() {
        this.props.swapi()
            .then(peopleList =>
                this.setState({peopleList}))
    }

    render() {
        const {peopleList} = this.state;
        const items = peopleList ? peopleList.map(item => {
                const label=this.props.labelData(item)
                return (
                    <li key={item.id}
                    onClick={()=>this.props.onSelectedItem(item.id)}>
                        {label}
                    </li>
                )
            }) : null;
            return <ul className="item-list list-group">
                    {items}
                </ul>
           }

    }

