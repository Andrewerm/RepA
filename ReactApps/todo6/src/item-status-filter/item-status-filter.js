import React, {Component} from 'react';

import './item-status-filter.css'

export default class ItemStatusFilter extends Component {
    render () {
        const {activeButton, clckButton}=this.props;
        const arr=['All', 'Active', 'Done'];
        const elements=arr.map(item=>(<button type="button"
                                              key={item}
                                              className={item===activeButton?"btn btn-info":"btn btn-outline-secondary"}
                                              onClick={()=>clckButton(item)}>
            {item}</button>));

        return(
            <div className="btn-group">
                {elements}
            </div>
        )
    }
};

