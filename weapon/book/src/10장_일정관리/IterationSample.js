import React, { useState} from 'react';

const IterationSample = () => {
    // const names = ['눈사람', '얼음', '눈', '바람'];
    // useState를 이용해서 상태 설정
    const [names, setNames] = useState([ // 객체 형태로 이루어진 배열
        { id: 1, text: '눈사람'},
        { id: 2, text: '얼음'},
        { id: 3, text: '눈'},
        { id: 4, text: '바람'}
    ]);
    const [inputText, setInputText] = useState('');
    const [nextId, setNextId] = useState(5); // 새로운 항목 추가시 사용할 id

    const onChange = e => setInputText(e.target.value);
    
    const onClick = () => {
        const nextNames = names.concat({
            id: nextId,
            text: inputText
        });
        setNextId(nextId+1); // nextId 값에 1을 더해준다.
        setNames(nextNames); // names 값을 업데이트한다.
        setInputText(''); // inputText를 비운다.
    };

    const onRemove = id => {
        const nextNames = names.filter(name => name.id !== id);
        setNames(nextNames);
    }

    const namelist = names.map(name => 
        <li key={ name.id } onDoubleClick={() => onRemove(name.id)}>
            { name.text }
        </li>);
    return (
        <>
            <input value={inputText} onChange={onChange} />
            <button onClick={onClick}>추가</button>
            <ul>{namelist}</ul>
        </>
    );
};

export default IterationSample;