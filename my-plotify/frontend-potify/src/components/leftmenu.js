import React from 'react'
import { FaSearch ,FaMusic,FaEllipsisH} from 'react-icons/fa';
import "../styles/leftmenu.css";
import {MenuList} from './menuList';
import { Menu } from './menu';
import {MenuPlayList} from "./MenuPlayList";
import {TrackList} from './TrackList'



function Leftmenu() {
    return(
        <div className='leftmenu'>
            <div className='logo-container'>
                <i><FaMusic/></i>
            <h2>plotify</h2>
        <i><FaEllipsisH/></i>
            </div>
            
            <div className='searchbox'>
                <input type='text' placeholder='search...'/>
                <i className='searchicon'>< FaSearch/></i>
            </div>
           <Menu title={"menu"} menuObject={MenuList}/>

           <MenuPlayList/>
           <TrackList/>
           
            </div>
            );
}

export { Leftmenu };