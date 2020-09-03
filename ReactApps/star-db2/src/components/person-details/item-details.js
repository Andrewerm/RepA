import React, {Component} from "react";
import SwapiService from "../../services/swapi-service";
import './person-details.css'
import Spinner from "../spinner";

export default class ItemDetails extends Component {

    // swapiSrv=new SwapiService();
    state={item:null, loading:false, image:null};

    updateInfo() {
        const {itemID, getData, getImageURL} = this.props;
        if (!itemID) {
            return
        }
        this.setState({loading: true});
        getData(itemID)
            .then(item => {
                this.setState({item, loading: false,
                image: getImageURL(item)})
            })
    }

    componentDidMount() {
        this.updateInfo()
    }

    componentDidUpdate(prevProps) {
        if (this.props.itemID!==prevProps.itemID) {this.updateInfo()}
    }

    render() {
        if (!this.state.item) {
            return <span>Select a person from a list</span>
        }
        if (this.state.loading) {return <Spinner/>}
        const {item, image}=this.state;
        return <div className='person-details card'>
                <img className='person-image'
                     src={image}
                     alt='character'/>
                <div className='card-body'>
                    <h4>{item.name}</h4>
                    <ul className='list-group list-group-flush'>
                        {React.Children.map(this.props.children,
                            ((child)=>React.cloneElement(child, {item})
                            ))}
                    </ul>
                </div>
            </div>
    }

}

const Record=({item, field, label})=>{

    return <li className='list-group-item'>
        <span className='term'>{label} </span>
        <span>{item[field]}</span>
    </li>
}

export {Record}