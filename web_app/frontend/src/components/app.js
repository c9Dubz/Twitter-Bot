import React, { Component } from "react";
import { render } from "react-dom";

export default class app extends Component{
    constructor(props) {
        supoer(props);
    }

    render() {
        return <h1>Test</h1>;
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);

