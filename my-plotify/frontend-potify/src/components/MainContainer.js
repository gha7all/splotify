import React from 'react'
//import  { useEffect } from "react";
import "../styles/Maincontainer.css";
// import { FaUsers } from "react-icons/fa";
// import { AudioList } from "./AudioList";
import { Banner } from "./Banner";

import '../styles/Maincontainer.css'

function MainContainer() {
    return(
        <div className='mainContainer'>
             <Banner />

        </div>
            );
}

export { MainContainer };