import React, { useState, useEffect } from 'react';
import './Avatar.css';

const Avatar = () => {
    const [avatars, setAvatars] = useState([]);

    useEffect(() => {
      const fetchDefaultAvatars = async () => {
        const response = await fetch('/api/avatars');
        if (response.ok) {
          const data = await response.json();
          setAvatars(data);
        }
      };
  
      fetchDefaultAvatars();
    }, []);

    console.log('avatars', avatars);
  
    return (
      <div>
        <h2>Default Avatars</h2>
        <div style={{ display: 'flex', gap: '20px' }}>
          {avatars.map((avatar) => (
            <div key={avatar.id}>
              <img
                src={avatar.avatar_image}
                alt={`Avatar ${avatar.id}`}
                width="100"
                height="100"
              />
            </div>
          ))}
        </div>
      </div>
    );
  };

export default Avatar;
