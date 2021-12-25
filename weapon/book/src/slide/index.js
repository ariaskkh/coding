// tailwind 적용 해야함..

import React, { useState } from 'react';
import styles from './index.module.css';

import babyshark from '../코딩애플실습/logo.svg';

export default function NewChallenge() {
  const [AlienName, setAlienName] = useState('');
  const [KindOfAlien, setKindOfAlien] = useState('null');

  return (
    <div className={styles.body}>
      <div className=" container top-60 border-gray-500 w-1/2 px-3 py-3 mb-3">
        <ul className="relative px-1 py-1 inline-flex">
          <li className=" mr-1 inline-block ">
            <a className="bg-white inline-block border-l border-t border-r rounded-t py-2 px-4 text-blue-700 font-semibold">
              기본
            </a>
          </li>
          <li className="mr-1 inline-block">
            <a className="bg-white inline-block py-2 px-4 text-blue-500  font-semibold">
              꾸미기
            </a>
          </li>
        </ul>
        <div className="border md:p-3">
          <div class={styles.slider}>
            <input
              type="radio"
              name="slide"
              id="slide1"
              //   onClick={() => AlienNum(1)}
            />
            <input
              type="radio"
              name="slide"
              id="slide2"
              //   onClick={() => AlienNum(2)}
            />
            <input
              type="radio"
              name="slide"
              id="slide3"
              //   onClick={() => AlienNum(3)}
            />
            <input
              type="radio"
              name="slide"
              id="slide4"
              //   onClick={() => AlienNum(4)}
            />
            <ul id="imgholder" class="imgs">
              <li>
                <img src={babyshark} alt={'이미지 로딩 실패'} />
              </li>
              <li>
                <img className="" src={babyshark} alt={'이미지 로딩 실패'} />
              </li>
              <li>
                <img src={babyshark} alt={'이미지 로딩 실패'} />
              </li>
              <li>
                <img src={babyshark} alt={'이미지 로딩 실패'} />
              </li>
            </ul>
            <div class={styles.bullets}>
              <label for="slide1">&nbsp;</label>
              <label for="slide2">&nbsp;</label>
              <label for="slide3">&nbsp;</label>
              <label for="slide4">&nbsp;</label>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
