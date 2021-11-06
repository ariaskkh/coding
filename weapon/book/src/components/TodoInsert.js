import React from 'react';
import { DiProlog } from 'react-icons/di';
import './TodoInsert.scss';

const TodoInsert = () => {
    return (
        <form className="TodoInsert">
            <input placeholder="할 일을 입력하거라"/>
            <button type="submit">
                <DiProlog />
            </button>
        </form>
    )
}

export default TodoInsert;