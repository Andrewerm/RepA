import React, {Component} from "react";
import './search-panel.css'




// const SearchPanel=()=> {
//     return <input placeholder='Введите текст'/>
//
// };
export default class SearchPanel extends Component {

    render () {
        const {searching, searchField}=this.props;
        return <input placeholder='Введите текст'
        onChange={(event)=>searching(event.target.value)}
        value={searchField}
        />}
}