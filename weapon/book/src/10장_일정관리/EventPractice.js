import React, { Component } from 'react';

class EventPractice extends Component {

    state = {
        message: ''
    }

    render() {
        return (
            <div>
                <h1>이벤트 연습</h1>
                <input
                    type="text"
                    name="message"
                    placeholder="아무거나 입력해 보세요"
                    value={this.state.message}
                    onChange={
                        (e) => {
                            // this.setState({
                                // message: e.target.value
                            // })
                            console.log(e.target.value);
                            }
                        }
                />
                <button onClick={
                    () => {
                        alert(this.state.message); // 클릭시 메시지 박스
                        this.setState({
                            message: '' // 다시 value 값 0
                        });
                    }
                }>확인</button>
            </div>
        );
    }
}

export default EventPractice;