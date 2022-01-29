import React from 'react';
import {FaPlus} from 'react-icons/fa';
import {BsMusicNoteList,BsTrash} from 'react-icons/bs';
import {playList} from "./PlayList"

function MenuPlayList() {
  return <div className='Pl-container'>
      <div className='namecontainer'>
            <p>playList</p>
            <i>
                <FaPlus/>
            </i>
      </div>
      <div className='scrollPlayList'>
          {
              playList && playList.map((list)=>( 
            <div className='PlayList'>
              {''}
              <i className='list'><BsMusicNoteList/></i>
              <p>{list.name}</p>
              <i className='trash'><BsTrash/></i>
          
            </div>))
          }
        
      </div>
  </div>;
}

export { MenuPlayList};
