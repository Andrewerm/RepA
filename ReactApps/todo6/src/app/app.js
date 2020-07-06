import React, {Component} from "react";
import Appheader from "../app-header";
import SearchPanel from "../search-panel";
import TodoList from "../todo-list";
import './app.css'
import ItemStatusFilter from "../item-status-filter";
import AddItem from "../add-item";


export default class App extends Component {
    maxIndex=100;

    createElement=(txt)=>{
        return {label:txt,
            id:this.maxIndex++,
            important: false,
            done:false
        }};

    state={todos: [this.createElement('Have a lunch'),
        this.createElement('Build awesome App'),
            this.createElement('Have a dinner')],
    searchField: '',
    activeButton: 'All'};

    deleteClck(id) {
        this.setState(({todos})=> {
            const idx=todos.findIndex((item)=>item.id===id);
            return {todos:[...todos.slice(0,idx), ...todos.slice(idx+1)]}
        })
    }

    addItemClck(txt) {
        this.setState(({todos})=> {
            const newAr=todos.slice();
            newAr.push(this.createElement(txt));
            return {todos: newAr}
        })
    }

    toggleProps(id,prop){
        this.setState(({todos})=>{
            const idx=todos.findIndex(index=>index.id===id);
            const newEl={...todos[idx],[prop]:!todos[idx][prop]};
            return {todos:[...todos.slice(0,idx), newEl, ...todos.slice(idx+1)]}
        })
    };

    searchFieldChange(txt) {
        this.setState(({searchField}) => {
            return {searchField: txt}
        });
    }

    clckButton(txt) {
        this.setState(({activeButton})=>{
            return {activeButton: txt}
        })

    }

    render() {
        const {todos,searchField, activeButton}=this.state;
        const countDone=todos.reduce((count, item)=>item.done?count+1:count,0);
        const filtered=todos
            .filter(item=>(item.label.toUpperCase().indexOf(searchField.toUpperCase())>=0))
            .filter(item=>activeButton==='All'?true:(activeButton==='Done'?item.done:!item.done));

        return <div className="todo-app">
            <Appheader toDo={todos.length-countDone} done={countDone}/>
            <SearchPanel searchField={searchField} searching={(txt)=>this.searchFieldChange(txt)}/>
            <ItemStatusFilter activeButton={activeButton} clckButton={txt=>this.clckButton(txt)}/>
            <TodoList todos={filtered}
                      deleteClck={(id)=>this.deleteClck(id)}
                      toggle={(id,prop)=>this.toggleProps(id,prop)}/>
            <AddItem addItemClck={(txt)=>this.addItemClck(txt)}/>
            </div>
    }
}

