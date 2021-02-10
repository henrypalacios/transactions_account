import React, { useEffect, useState } from "react";
import Accordion from "react-bootstrap/Accordion";

import CardItem from "../card/CardItem";
import "./Accordion.css";

const AccordionItem = () => {
  const [items, setItems] = useState([]);
  const [isLoaded, setIsLoaded] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/transactions")
      .then((res) => res.json())
      .then(
        (result) => {
          setItems(result);
          setIsLoaded(true);
        },
        (error) => {
          setIsLoaded(false);
          setError(error);
        }
      );
  }, []);

  const renderLoading = () => {
    let html = <div>Loading...</div>;

    if (error) {
      html = <div>Error: {error.message}</div>;
    }
    return html;
  };

  console.log(items);

  return (
    <div className="header container">
      {!isLoaded ? (
        renderLoading()
      ) : (
        <Accordion>
          <div className="card-header container">
            <div className="row">
              <div className="col-sm">Type</div>
              <div className="col-sm">Amount</div>
            </div>
          </div>
          {items.map((item) => (
            <CardItem {...item} />
          ))}
        </Accordion>
      )}
    </div>
  );
};

export default AccordionItem;

