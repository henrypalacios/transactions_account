import React, { useState } from "react";
import Accordion from "react-bootstrap/Accordion";
import Card from "react-bootstrap/Card";
import Badge from "react-bootstrap/Badge";

import "./CardItem.css";

const CardItem = (props) => {
  const { id, type, amount, effectiveDate } = props;
  const colorLabel = type == "credit" ? "positive" : "negative";

  return (
    <Card>
      <Accordion.Toggle as={Card.Header} eventKey={id}>
        <div class="row">
          <div className={`col-sm ${colorLabel}`}>{type}</div>
          <div className="col-sm">{amount}</div>
        </div>
      </Accordion.Toggle>
      <Accordion.Collapse eventKey={id}>
        <Card.Body>
          <div>Id: {id}</div>
          <div>Type: {type}</div>
          <div>Amount: {amount}</div>
          <div>Date: {effectiveDate}</div>
        </Card.Body>
      </Accordion.Collapse>
    </Card>
  );
};

export default CardItem;

