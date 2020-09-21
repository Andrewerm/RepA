import React, {Component} from "react";
import ErrorIndicator from "../error-indicator";
export default class  SelectService extends (Component)
{
    state={hasError:false}

    componentDidCatch() {
        this.setState({hasError:true})
    }


    render()
    {
        if (this.state.hasError) {
            return <ErrorIndicator/>
        }
        const {wItem}=this.props
        return <div className='person-details card'> Погода {wItem.srvName} {wItem.current_temp}</div>

    }
}

