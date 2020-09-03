import React, {Component} from "react";
import './search-panel.css'

export default class SearchPanel extends Component {

    render() {
        const searchtext='search text';
          return <input className='search-input'
                      placeholder={searchtext}
          onChange={(event)=>this.props.searchUpdate(event.target.value)}/>;
    }
}


