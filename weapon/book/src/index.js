// // 6장, 10장, 코딩코딩실습

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
// import App from './6장_컴포넌트 반복/App';
// import App from './10장_일정관리/App';
// import App from './애플코딩실습/App';
// import reportWebVitals from './reportWebVitals';
// import App from './velopert_redux/actions/App';
import App from './carousel/App';
// import App from './slide';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root'),
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

/////////////////////////////////////////////////////////////////////////
// 13장

// import React from 'react';
// import ReactDOM from 'react-dom';
// import { BrowserRouter } from 'react-router-dom';
// import './index.css';
// // import reportWebVitals from './reportWebVitals';
// import App from './13장_react_router/App';

// ReactDOM.render(
//   <BrowserRouter>
//     <App />
//   </BrowserRouter>,
//   document.getElementById('root')
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// // reportWebVitals();

///////////////////////////////////////////////////////////////////////////
// 17장

// import React from 'react';
// import ReactDOM from 'react-dom';
// import './index.css';
// import App from './17장_리덕스/App';
// import { createStore } from 'redux';
// import { Provider } from 'react-redux';
// import { composeWithDevTools } from 'redux-devtools-extension';
// import rootReducer from './17장_리덕스/modules';
// // import reportWebVitals from './reportWebVitals';

// const store = createStore(rootReducer, composeWithDevTools());

// ReactDOM.render(
//   <Provider store={store}>
//     <App />
//   </Provider>,
//   document.getElementById('root')
// );

///////////////////////////////////////////////////////////////
// veopert_redux

// import React from 'react';
// import ReactDOM from 'react-dom';

// import App from './velopert_redux/components/App';

// import { createStore } from 'redux';
// import reducers from './velopert_redux/reducers';

// import { Provider } from 'react-redux';

// const store = createStore(reducers);

// ReactDOM.render(
//   <Provider store={store}>
//     <App />
//   </Provider>,
//   document.getElementById('root'),
// );

////////////////////////////////////////////////////////////
// 코딩애플-redux
// import React from 'react';
// import ReactDOM from 'react-dom';
// import { Provider } from 'react-redux';
// import { createStore } from 'redux';
// import App from './코딩애플_redux/App.js';

// const 체중 = 100;

// function reducer(state = 체중, action) {
//   if (action.type === '증가') {
//     state++;
//     return state;
//   } else if (action.type === '감소') {
//     state--;
//     return state;
//   } else {
//     return state;
//   }
// }

// let store = createStore(reducer);

// ReactDOM.render(
//   <React.StrictMode>
//     <Provider store={store}>
//       <App />
//     </Provider>
//   </React.StrictMode>,
//   document.getElementById('root'),
// );
