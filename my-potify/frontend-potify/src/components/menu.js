import React from 'react';


function Menu({title , menuObject}) {
    return (
        <div className='menuContainer'>
            <p className='title'>{title}</p>
            <ul>
                {
                    menuObject && menuObject.map((menu)=>(
                        <li>
                        {''}
                        <a href="a"><i>{menu.icon}</i>
                        <span>{menu.name}</span></a>
                        </li>
                    ))
                    
                }
            </ul>
        </div>
    );
}

export {Menu};
