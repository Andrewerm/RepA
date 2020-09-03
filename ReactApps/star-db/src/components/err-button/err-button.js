import React, {Component} from "react";

export default class ErrBatton extends Component {
    state={
        renderError:false
    }

    render() {
        console.log('render')
        if (this.state.renderError) {
            this.foo.bar=0
        }
        return <button
            className="error-button btn btn-danger btn-lg"
            onClick={()=> this.setState({renderError: true})}>
            ThrowError
        </button>
    }
}
