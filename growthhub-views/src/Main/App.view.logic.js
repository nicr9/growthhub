import React from 'react'
import App from './App.view.js'

export default class AppLogic extends React.Component {
  state = {
    accepted: [],
    isMain: true,
    isSelect: false,
    isSubmit: false,
    isFinalMessage: false,
  }

  main = () => {
    this.setState({
      isMain: true,
      isSelect: false,
      isSubmit: false,
      isFinalMessage: false,
    })
  }

  select = () => {
    this.setState({
      isMain: false,
      isSelect: true,
      isSubmit: false,
      isFinalMessage: false,
    })
  }

  finalMessage = () => {
    this.setState({
      isMain: false,
      isSelect: false,
      isSubmit: false,
      isFinalMessage: true,
    })
  }

  maybeSubmit = (isSubmit, accepted) => {
    this.setState({
      isSubmit,
      accepted
    })
  }

  render() {
    return (
      <App
        {...this.props}
        {...this.state}
        main={this.main}
        select={this.select}
        maybeSubmit={this.maybeSubmit}
        finalMessage={this.finalMessage}
      />
    )
  }
}
