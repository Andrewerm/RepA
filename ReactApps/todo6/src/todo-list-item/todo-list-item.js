import React,{Component} from "react";
import './todo-list-item.css'

export default class TodoListItem extends Component{

    render() {
        const {deleteClck, action}=this.props;
        const {label, done, important}=this.props.items
        let style='todo-list-item';
        if (done) {style+=' done'}
        if (important) {style+=' important'}
        return (<span className={style}>
            <span className='todo-list-item-label' onClick={()=>action('done')}>{label}</span>
      <button type="button"
                   className="btn btn-outline-success btn-sm float-right" onClick={()=>action('important')}>
        <i className="fa fa-exclamation" />
      </button>

      <button type="button"
              className="btn btn-outline-danger btn-sm float-right" onClick={deleteClck}>
        <i className="fa fa-trash-o" />
      </button>
        </span>)
    }

}