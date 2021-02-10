import React from 'react';
import ReactDOM from 'react-dom';

import AccordionItem from './components/accordion/AccordionItem';
import './App.css';

const App = () => {
	return (
		<div className="header container">
			<AccordionItem>
			</AccordionItem>
		</div>
	);
};

ReactDOM.render(<App/>, document.querySelector('#root'))