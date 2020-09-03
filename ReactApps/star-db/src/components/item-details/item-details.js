import React, {Component} from "react";
import Spinner from "../spinner";
import ErrBatton from "../err-button";
import './person-details.css'

export default class ItemDetails  extends Component{

    state={item:null,
        loading:false,
        image: null};

    componentDidMount() {
        this.updateItem()
    }

    updateItem () {
        const {itemId, getData, getImageUrl}=this.props;
        if (!itemId) {return}
        this.setState({loading:true});
        getData(itemId)
                .then(item=> {this.setState({item, loading:false,
                image: getImageUrl(item)})})
    }

    componentDidUpdate(prevProps){
        if (this.props.itemId!==prevProps.itemId) {
            this.updateItem()
        }
            }

    render() {
        if (!this.state.item) {
            return <span>Select a person from a list</span>
        }
        const {item, image}=this.state
        const spinner=<Spinner/>;
        const element=<div className='person-details card'>
            <img className='person-image'
                 src={image}
                 alt='character'/>
            <div className='card-body'>
                <h4>{item.name}</h4>
                <ul className='list-group list-group-flush'>
                    {React.Children.map(this.props.children,
                        ((child,idx)=>React.cloneElement(child, {item})
                    ))}
                </ul>
            </div>
            </div>;
        const output=this.state.loading?spinner:element;
        return <React.Fragment>
            {output}
            <ErrBatton/>
        </React.Fragment>
 }
}


const Record=({item, field, label})=> {
    return <li className='list-group-item'>
        <span className='term'>{label}</span>
        <span>{item[field]}</span>
    </li>

}
export  {Record}


