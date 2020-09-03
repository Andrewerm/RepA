import React, {Component} from "react";

import SwapService from "../../services/swapi-service";
import withData from "../hoc-helpers";

const ItemList=({data,onItemSelected, children})=> {

    function renderItem(arr) {
        return arr.map((item)=> {
            const {id}=item;
            const label=children(item);
            return (
                <li className="list-group-item"
                    key={id}
                    onClick={()=> onItemSelected(id)}>
                    {label}
                </li>
            )
        })
    }
        const items=renderItem(data)
        return (
            <ul className="item-list list-group">
                {items}
            </ul>
        )

}




const {getAllPeople}= new SwapService()
export default withData(ItemList, getAllPeople)