import React from 'react';
import './TodoTemplate.scss';

const TodoTemplate = ({ children }) =>{
    return (
        <div className="TodoTemplate">
            <div className="app-title">(니가 안할 것 같은) 일정 관리</div>
            <div className="content">{ children }</div>
        </div>
    );
};

export default TodoTemplate;