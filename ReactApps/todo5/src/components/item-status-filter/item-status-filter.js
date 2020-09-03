import React, {Component} from 'react';

import './item-status-filter.css';

export default class ItemStatusFilter extends Component {
    render () {
        const {buttons, clckButton}=this.props;
        const arr=['btn '+(buttons.all?'btn-info':'btn-outline-secondary'),
            'btn '+(buttons.active?'btn-info':'btn-outline-secondary'),
            'btn '+(buttons.done?'btn-info':'btn-outline-secondary')
        ];

        return(
            <div className="btn-group">
                <button type="button"
                        className={arr[0]}
                        onClick={()=>clckButton('all')}>All</button>
                <button type="button"
                        className={arr[1]}
                        onClick={()=>clckButton('active')}>Active</button>
                <button type="button"
                        className={arr[2]}
                        onClick={()=>clckButton('done')}>Done</button>
            </div>
        )
    }
};
