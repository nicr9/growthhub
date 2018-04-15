import Spinner from './Spinner.js'
import staticData from './select-data.json'
import Fetch from 'holen'
import Select from './Select.view.js'
import React from 'react'

const morph = data => {
  return {
    ...data,
    lenders: data.lenders.map((item, index) => ({
      id: index,
      ...item,
      reasons: item.reasons.map(reason => ({
        id: reason,
        reason,
      })),
    })),
  }
}

class SelectOverLogic extends React.Component {
  state = {
    lenders: this.props.lenders.map(item => ({
      ...item,
      isSelected: false,
    })),
  }

  toggleSelect = id => {
    this.setState(
      {
        lenders: this.state.lenders.map(
          item =>
            item.id === id
              ? {
                  ...item,
                  isSelected: !item.isSelected,
                }
              : item
        ),
      },
      () => {
        const somethingIsSelected = this.state.lenders.some(
          item => item.isSelected
        )

        this.props.maybeSubmit(somethingIsSelected)
      }
    )
  }

  render() {
    return <Select {...this.props} {...this.state} select={this.toggleSelect} />
  }
}

export default class SelectLogic extends React.Component {
  state = {
    didFetch: false,
    data: null,
  }

  render() {
    if (!this.state.didFetch) {
      return (
        <Fetch url="http://206.189.112.64:5000/">
          {({ data: maybeData, error, fetching }) => {
            if (fetching) return <Spinner width="100%" />

            const data = morph(error ? staticData : maybeData)
            this.setState({ didFetch: true, data })
            return null
          }}
        </Fetch>
      )
    }

    return <SelectOverLogic {...this.props} {...this.state.data} />
  }
}
