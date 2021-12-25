// actionTypes를 불러옴
import * as types from '../actions/ActionTypes';

// reducer 초기 상태 정하기. 상수 형태의 객체로 정의
const initialState = {
  number: 0,
  dummy: 'dumbdumb',
  dumbObject: {
    d: 0,
    u: 1,
    m: 2,
    b: 3,
  },
};

export default function counter(state = initialState, action) {
  switch (action.type) { // dispatch로부터 action 객체를 받음
    case types.INCREMENT:
      // number 값, dumbOject의 u 값 덮어 씌움. ...state를 안쓰면 사용하지 않는 dummy가 지워짐
      return {
        ...state,
        number: state.number + 1,
        dumbObject: { ...state.dumbObject, u: 0 },
      };
    case types.DECREMENT:
      return {
        ...state,
        number: state.number - 1,
      };
    default:
      return state;
  }
}
