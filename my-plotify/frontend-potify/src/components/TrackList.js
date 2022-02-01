import React from 'react';
import {FaDesktop} from 'react-icons/fa';
import {BsVolumeUpFill,BsMusicNoteList} from 'react-icons/bs';
import Track from '../img/track.png' 

function TrackList() {
  return (
  <div className='trackList'>
      <div className='top'>
        <img alt='' src={Track}></img>
        <p>I think of you <span>adele</span></p>
     </div>
      <div className='bottom'>
          <i><BsVolumeUpFill/></i>
          <input type="range"></input>
          <i><BsMusicNoteList/></i>
          <i><FaDesktop/></i>
      </div>
         </div>
  );
  
}

export {TrackList};
