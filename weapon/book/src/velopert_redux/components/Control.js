import React, { Component } from 'react';

// function createWarning(funcName) {
//   return () => console.warn(funcName + ' is not defined');
// }
// const defaultProps = {
//   onPlus: createWarning('onPlus'),
//   onSubtract: createWarning('onSubtract'),
//   onRandomizeColor: createWarning('onRandomizeColor'),
// };

class Control extends Component {
  //   constructor(props) {
  //     super(props);
  //   }

  render() {
    return (
      <div>
        <button onClick={this.props.onPlus}>+</button>
        <button onClick={this.props.onSubtract}>-</button>
        <button onClick={this.props.onRandomizeColor}>Randomize Color</button>
      </div>
    );
  }
}

export default Control;
