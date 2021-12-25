import * as types from '../actions/ActionTypes';

const initialState = {
  // 초기 상태
  color: [255, 255, 255], // rgb 형태
};

export default function ui(state = initialState, action) {
  if (action.type === types.SET_COLOR) {
    return {
      color: action.color,
    };
  } else {
    return state;
  }
}
