import React, {Component} from "react";
import './add-new-item.css'

export default class AddNewItem extends Component {
    state={
        label: ''
    };

    onlabelChange=(e)=> {
        this.setState({label: e.target.value})
    };

    onSubmit=(e)=>{
        e.preventDefault();
        this.props.action(this.state.label)
        this.setState({label: ''})
    };

    render() {
        return(
        <form className='item-add-form d-flex' onSubmit={this.onSubmit}>
            <input type='text' className='form-control' onChange={this.onlabelChange}
            placeholder='Что нужно сделать'
            value={this.state.label}/>
            <button type="submit"
                    className='btn btn-outline-secondary'>добавить элемент
            </button>
        </form>)
    }
  };




