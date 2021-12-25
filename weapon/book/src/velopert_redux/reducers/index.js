import { combineReducers } from 'redux';
import counter from './counter';
import ui from './ui';

// counter, ui 둘다 실행됨
const reducers = combineReducers({
  counter,
  ui,
});

export default reducers;
