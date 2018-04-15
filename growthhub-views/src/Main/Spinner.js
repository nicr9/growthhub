// @view
import * as Spinners from 'react-spinners'
import React from 'react'

const Spinner = ({ type, ...props }) => {
  const Type = Spinners[type]
  return <Type loading={true} {...props} />
}
Spinner.defaultProps = {
  type: 'BarLoader',
}
export default Spinner
