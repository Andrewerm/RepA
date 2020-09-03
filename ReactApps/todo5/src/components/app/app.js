import Appheader from "../app-header";
import SearchPanel from "../search-panel";
import TodoList from "../todo-list";
import React,{Component} from "react";
import ItemStatusFilter from "../item-status-filter";
import AddNewItem from "../add-new-item";

export default class App extends Component {
    maxID=100;
    state={
    todoData: [
        this.createTodoItem('Drink Cofee'),
        this.createTodoItem('Build App'),
        this.createTodoItem('Walking')],
    searchTxt: '',
    buttons: {all:true, active:false, done:false}
};

    createTodoItem(label) {
        return {
            label,
            important: false,
            done: false,
            id: this.maxID++
        }
    }

    deleteItem=(id)=> {
        this.setState( ({todoData})=> {
            const idx=todoData.findIndex(item=> item.id===id);
            const newarray=[...todoData.slice(0,idx), ...todoData.slice(idx+1)];
            return {todoData:newarray}
        })
    };
    addItem=(text)=>{
        this.setState(({todoData})=>{
        const newArr=todoData.slice();
        newArr.push(this.createTodoItem(text));
        return {todoData: newArr}
    })
    };

    toggleProperty(id, propName) {
        this.setState(({todoData})=>{
            const idx=todoData.findIndex(item=> item.id===id);
            const oldItem=todoData[idx];
            const newItem={...oldItem, [propName]:!oldItem[propName]};
            return {todoData:[...todoData.slice(0,idx), newItem, ...todoData.slice(idx+1)]}
        });
    };

    searching(txt) {
        this.setState(()=>{return {searchTxt:txt}});
        };

    clickButton(bt) {
        this.setState(({buttons})=>{
            let newObj={all:false, active:false, done:false};
            newObj[bt]=true;
            return {buttons:newObj}
        });
    }

    onToggleImportant=(id)=>this.toggleProperty(id,'important');
    onToggleDone=(id)=>this.toggleProperty(id,'done');

    render() {
        const {todoData, searchTxt, buttons}=this.state;
        const dones=todoData.reduce((count, current)=>{return current.done?count+1:count},0);
        const filtertoDo=todoData
            .filter(item=>buttons.all?true:(buttons.done?item.done:!item.done))
            .filter(item=>item.label.toUpperCase().indexOf(searchTxt.toUpperCase())>=0);

        return <div className="todo-app">
            <Appheader toDo={todoData.length-dones} done={dones}/>
            <div className='top-panel d-flex'>
                <SearchPanel searchUpdate={(txt)=>this.searching(txt)}/>
                <ItemStatusFilter buttons={this.state.buttons} clckButton={(bt)=>this.clickButton(bt)}/>
            </div>
            <TodoList todos={filtertoDo}
                      onDeleted={this.deleteItem}
                      onToggleImportant={this.onToggleImportant}
                      onToggleDone={this.onToggleDone}
            />
            <AddNewItem action={this.addItem}/>
        </div>
    }


}