import Spinner from './Spinner.js'
import staticData from './select-data.json'
import Fetch from 'holen'
import Select from './Select.view.js'
import React from 'react'

export default class SelectLogic extends React.Component {
  render() {
    return (
      <Fetch url="http://206.189.112.64:5000/">
        {({ data: maybeData, error, fetching }) => {
          if (fetching) return <Spinner width="100%" />

          const data = error ? staticData : data

          return <Select {...this.props} {...data} />
        }}
      </Fetch>
    )
  }
}
