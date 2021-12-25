import * as types from './ActionTypes';

export function increment() {
  return {
    // type: types.INCREMENT,
    type: 'INCREMENT',
  };
}

export function decrement() {
  return {
    type: types.DECREMENT,
  };
}

export function setColor(color) {
  return {
    type: types.SET_COLOR,
    color, // color: color와 동일한 의미
  };
}
