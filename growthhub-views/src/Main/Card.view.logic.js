import React from 'react'
import Card from './Card.view.js'

const CardLogic = props => (
  <Card {...props} isOk={props.reasons.length === 0} />
)
export default CardLogic
