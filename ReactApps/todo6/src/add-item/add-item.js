import React, {Component} from 'react'
import './add-item.css'

export default class AddItem extends Component  {
    state={label: ''};

    onLabelChange=(event)=> {
        this.setState({label:event.target.value});
    };

    onSubmit=(e)=>{
        e.preventDefault();
        if (this.state.label!=='')
        {this.props.addItemClck(this.state.label)
        this.setState({label:''})}
    }

    render() {
        return <form className='item-add-form d-flex' onSubmit={this.onSubmit}>
            <input type='text'
            className='form-control'
            onChange={this.onLabelChange}
            placeholder='Что надо сделать'
            value={this.state.label}
                />
            <button className='btn btn-outline-secondary'> Добавить элемент </button>

        </form>
    }


}
