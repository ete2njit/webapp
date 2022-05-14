import * as React from 'react';
import PropTypes from 'prop-types';
import { Socket } from './Socket';
import '../static/informationstyle.css';

export function Information({ username }) {
  const [users, setUsers] = React.useState([]);

  function getUsers() {
    React.useEffect(() => {
      Socket.on('all users', (data) => {
        setUsers((users) => data.allUsers);
      });
    }, []);
  }

  function userConnected() {
    React.useEffect(() => {
      Socket.on('user connected', (data) => {
        setUsers((users) => [...users, data.name]);
      });
    }, []);
  }

  function userDisconnected() {
    React.useEffect(() => {
      Socket.on('user disconnected', (data) => {
        const newList = users.filter((item) => item !== data.name);
        setUsers(newList);
      });
    }, []);
  }

  getUsers();
  userConnected();
  userDisconnected();

  return (
    <div className="information-window">
      <div className="information-content">
        <h3>
          Logged in as
          { username }
        </h3>
        <p>
          Current users (
          { users.length }
          ):
        </p>
        <div className="users-box">
          {users.map((user) => (
            <div key={user.id}>
              <span key={user.id}>{ user }</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

Information.propTypes = {
  username: PropTypes.string.isRequired,
};
