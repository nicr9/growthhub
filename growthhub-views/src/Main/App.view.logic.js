import React from 'react'
import App from './App.view.js'

export default class AppLogic extends React.Component {
  state = {
    isMain: true,
    isSelect: false,
  }

  main = () => {
    this.setState({
      isMain: true,
      isSelect: false,
    })
  }

  select = () => {
    this.setState({
      isMain: false,
      isSelect: true,
    })
  }

  render() {
    return (
      <App
        {...this.props}
        {...this.state}
        main={this.main}
        select={this.select}
      />
    )
  }
}
