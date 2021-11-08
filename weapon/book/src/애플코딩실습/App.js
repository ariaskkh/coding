/* eslint-disable */

import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';


function App() {
  
  let posts = '연쇄삽입마333';
  let [글제목,글제목변경] = useState(["남자 코트 추천", "강남 우동 맛집", "게이 바 추천"]); // destructuring
  let [따봉, 따봉변경] = useState(0);
  let 제목변경 = ["여자 코트 추천", "강남 우동 맛집", "게이 바 추천"]
  function 제목바꾸기() {
    var newArray = [...글제목];
    newArray.sort();
    글제목변경(newArray);
    // 글제목변경(["여자 코트 추천", "강남 우동 맛집", "게이 바 추천"]);
  }

  return (
    <div className="App"> 
      <div className="black-nav">
        <div> 정글 Blog</div>
      </div>
      <div className="list">
        <h3> { 글제목[0] } <span onClick ={ ()=>{ 따봉변경(따봉+1) }}>👍</span> {따봉} </h3>
        <p>2월 17일 발행</p>
        <button onClick= {제목바꾸기}>똥버튼 ! 💩</button>
        <hr/>
      </div>
      <div className="list">
        <h3> { 글제목[1] }</h3>
        <p>2월 17일 발행</p>
        <hr/>
      </div> 
      <div className="list">
        <h3> { 글제목[2] }</h3>
        <p>2월 17일 발행</p>
        <hr/>
      </div> 

      <Modal/>
      
      
      <img src={ logo }/> 

    </div>
  );
}

function Modal() {
  return(
  <div className="modal">
    <h1>제목</h1>
    <p>날짜</p>
    <p>상세내용</p>
  </div>
  )
}

export default App;
