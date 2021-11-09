import { createStore } from 'redux';

// DOM 레퍼런스 만들기
// UI 관리시 별도의 UI를 사용하지 않기 때문에 DOM을 직접 수정
// DOM 노드를 가리키는 값을 미리 선언해준다.
const divToggle = document.querySelector('.toggle');
const counter = document.querySelector('h1');
const btnIncrease = document.querySelector('#increase');
const btnDecrease = document.querySelector('#decrease');

// 액션의 타입(이름)과 생성 함수 정의
const TOGGLE_SWITCH = 'TOGGLE_SWITCH';
const INCREASE = 'INCREASE';
const DECREASE = 'DECREASE';

// 액션 객체를 만드는 액션 생성 함수를 작성
const toggleSwitch = () => ({ type: TOGGLE_SWITCH});
const increase = difference => ({ type: INCREASE, difference });
const decrease = () => ({ type: DECREASE });

// 초기값 설정
const initialState = {
    toggle: false,
    counter: 0
};

// reducer : 변화를 일으키는 함수
// 리듀서 함수 정의. 함수의 파라미터로 state와 action 값을 받아 옵니다.
// state가 undefined일 때는 initialState를 기본값으로 사용
function reducer(state = initialState, action) {
    // action.type에 따라 다른 작업을 처리함
    switch (action.type) {
        case TOGGLE_SWITCH:
            return {
                ...state, // 불변성 유지를 해 주어야 함수
                toggle: !state.toggle
            };
        case INCREASE:
            return {
                ...state,
                counter: state.counter + action.difference
            };
        case DECREASE:
            return {
                ...state,
                counter: state.counter - 1
            };
        default:
            return state;
        }
}

// 스토어 만들기
const store = createStore(reducer);

// render 함수 만들기 - 상태 업데이트될 때마다 호출됨.
const render = () => {
    const state = store.getState(); // 현재 상태를 불러옵니다.
    // 토글 처리
    if (state.toggle) {
        divToggle.classList.add('active');
    } else {
        divToggle.classList.remove('active');
    }
    // 카운터 처리
    counter.innerText = state.counter;
};

render();
// 상태 바뀔 때마다 방금 만든 render함수가 호출되도록 함. 내장함수 subscribe 이용
store.subscribe(render);

// 액션 발생시키기 == dispatch. 파라미터는 액션 객체를 넣어준다.
divToggle.onclick = () => {
    store.dispatch(toggleSwitch());
};
btnIncrease.onclick = () => {
    store.dispatch(increase(1));
};
btnDecrease.onclick = () => {
    store.dispatch(decrease());
};