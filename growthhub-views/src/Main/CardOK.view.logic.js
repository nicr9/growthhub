import CardOK from './CardOK.view.js'
import React from 'react'

export default props => (
  <CardOK {...props} select={() => props.select(props.id)} />
)
