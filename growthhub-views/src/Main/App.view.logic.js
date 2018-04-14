import React from 'react'
import App from './App.view.js'

export default class AppLogic extends React.Component {
  render() {
    return <App {...this.props} />
  }
}